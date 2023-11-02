from transformers import T5ForConditionalGeneration, AutoModelForSeq2SeqLM
import torch
from transformers import Trainer, Seq2SeqTrainer
from transformers import AutoConfig
import torch.nn.functional as F
from typing import Optional, Tuple, Union, Dict



class CustomTrainer(Seq2SeqTrainer):
    def compute_loss(self, model, inputs, return_outputs=False):
        loss, outputs = super().compute_loss(model, inputs, return_outputs=True)

        self.log({"distillation_loss": torch.mean(outputs["distillation_loss"]).item()})
        self.log({"ce_loss": torch.mean(outputs["ce_loss"]).item()})
        return (loss, outputs) if return_outputs else loss
        


class SD_T5ForConditionalGeneration(T5ForConditionalGeneration):
    def __init__(self, config):
        super(SD_T5ForConditionalGeneration, self).__init__(config)
        self.teacher_model = None
        self.register_buffer('teacher_model_registered', torch.tensor(0))
        
    @classmethod
    def from_pretrained_with_teacher(cls, student_pretrained_model_name_or_path, teacher_model, config):
        # config = kwargs.pop("config", None)
        # if config is None:
        #     config = AutoConfig.from_pretrained(student_pretrained_model_name_or_path, **kwargs)
        student_model = cls.from_pretrained(student_pretrained_model_name_or_path, config=config)
        student_model.teacher_model = teacher_model
        return student_model
    
    def save_pretrained(self, save_directory, **kwargs):
        # Store teacher_model temporarily and remove it from the object
        teacher_model_temp = None
        if hasattr(self, 'teacher_model'):
            teacher_model_temp = self.teacher_model
            del self.teacher_model

        # Save the student model
        super().save_pretrained(save_directory, **kwargs)

        # Restore the teacher_model if it was temporarily stored
        if teacher_model_temp is not None:
            self.teacher_model = teacher_model_temp
    
    def forward(self,
        input_ids: Optional[torch.LongTensor] = None,
        attention_mask: Optional[torch.FloatTensor] = None,
        decoder_input_ids: Optional[torch.LongTensor] = None,
        decoder_attention_mask: Optional[torch.BoolTensor] = None,
        head_mask: Optional[torch.FloatTensor] = None,
        decoder_head_mask: Optional[torch.FloatTensor] = None,
        cross_attn_head_mask: Optional[torch.Tensor] = None,
        encoder_outputs: Optional[Tuple[Tuple[torch.Tensor]]] = None,
        past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = None,
        inputs_embeds: Optional[torch.FloatTensor] = None,
        decoder_inputs_embeds: Optional[torch.FloatTensor] = None,
        labels: Optional[torch.LongTensor] = None,
        use_cache: Optional[bool] = None,
        output_attentions: Optional[bool] = None,
        output_hidden_states: Optional[bool] = None,
        return_dict: Optional[bool] = None,
    ):  
        # 调用父类的 forward 函数
        outputs = super().forward(input_ids, attention_mask, decoder_input_ids, decoder_attention_mask, head_mask, decoder_head_mask, cross_attn_head_mask,
                                  encoder_outputs, past_key_values, inputs_embeds, decoder_inputs_embeds, labels, use_cache, output_attentions, output_hidden_states, return_dict)
        # # 使用教师模型生成教师分布
        with torch.no_grad():
            teacher_outputs = self.teacher_model(input_ids, attention_mask, decoder_input_ids, decoder_attention_mask, head_mask, decoder_head_mask, cross_attn_head_mask,
                                  encoder_outputs, past_key_values, inputs_embeds, decoder_inputs_embeds, labels, use_cache, output_attentions, output_hidden_states, return_dict)
        
        # directly distillation
        # outputs = self.direct_distillation(outputs, teacher_outputs)
        
        # top_p_distillation 0.9
        outputs = self.top_p_distillation(outputs, teacher_outputs)
        
        outputs["ce_loss"] = outputs.loss
        outputs.loss = outputs["distillation_loss"] + outputs.loss
        
        return outputs
    
    def direct_distillation(self, student_outputs, teacher_outputs):
        # 计算学生模型与教师分布之间的损失，将其添加到输出中
        student_probs = F.softmax(student_outputs.logits, dim=-1)
        teacher_probs = F.softmax(teacher_outputs.logits, dim=-1)

        distillation_kl_div_loss = F.kl_div(torch.log(student_probs), teacher_probs, 
                                            # reduction='batchmean'
                                            )
        student_outputs["distillation_loss"] = distillation_kl_div_loss
        return student_outputs
    
    def top_p_distillation(self, student_outputs, teacher_outputs):
        # 设置阈值
        threshold = 0.99
        student_probs = F.softmax(student_outputs.logits, dim=-1)
        teacher_probs = F.softmax(teacher_outputs.logits, dim=-1)
        
        # 对概率分布进行排序并获取索引
        sorted_probs, sorted_indices_t = torch.sort(teacher_probs, descending=True) # sorted_indices_t [batch, length, V]
        
        # 选择累积概率大于等于阈值的索引
        cumulative_probs_t = torch.cumsum(sorted_probs, dim=-1)
        
        sorted_indices_to_remove = cumulative_probs_t > threshold # [batch, length, V]

        # Shift the indices to the right to keep also the first token above the threshold
        sorted_indices_to_remove[..., 1:] = sorted_indices_to_remove[..., :-1].clone()
        sorted_indices_to_remove[..., 0] = 0

        # scatter sorted tensors to original indexing
        # indices_to_remove = torch.gather(sorted_indices_to_remove, 1, sorted_indices_t)
        indices_to_remove = sorted_indices_to_remove.scatter(2, sorted_indices_t, sorted_indices_to_remove)
        # 计算KL散度
        kl_div = F.kl_div(
            torch.log(student_probs), teacher_probs, reduction="none"
            )

        # 将忽略位置的KL散度设为0
        kl_div[indices_to_remove] = 0
        
        num = torch.sum(~indices_to_remove, dim=-1)
        distillation_kl_div_loss = torch.mean(kl_div.sum(dim=-1) / num)
        student_outputs["distillation_loss"] = distillation_kl_div_loss
        
        return student_outputs
        
        # print(indices_to_remove)
        # print(distillation_kl_div_loss[1 - indices_to_remove].size())

        # Back to unsorted indices and set them to -infinity
        # indices_to_remove = sorted_indices_t[sorted_indices_to_remove]
        # print(sorted_indices_to_remove)
        # print(sorted_indices_t.size())
        
        # student_probs[indices_to_remove] = 1e-9
        # teacher_probs[indices_to_remove] = 0
        
        # selected_indices_s = (cumulative_probs_s >= threshold).sum(dim=1)
        # selected_indices_t = (cumulative_probs_t <= threshold).sum(dim=1)
        # print(selected_indices_t)
        # 使用选定的索引计算 KL 散度
        # s_selected = torch.stack([student_probs[i, selected_indices_t[i, :n]] for i, n in enumerate(selected_indices_t)])
        # t_selected = torch.stack([teacher_probs[i, sorted_indices_t[i, :n]] for i, n in enumerate(selected_indices_t)])

        # distillation_kl_div_loss = student_probs * (torch.log(student_probs) - torch.log(teacher_probs))

        # distillation_kl_div_loss = torch.mean(torch.sum(distillation_kl_div_loss[1 - indices_to_remove], dim=-1), dim=-1)
        # distillation_kl_div_loss = torch.mean(distillation_kl_div_loss)
