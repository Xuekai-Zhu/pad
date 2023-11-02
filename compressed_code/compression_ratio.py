from transformers import AutoTokenizer, AutoModel, AutoModelForSeq2SeqLM, LlamaTokenizer, LlamaForCausalLM
import pandas as pd
from delte_annopate import load_json_file
import json
# from torch import Dataset
from torch.utils.data import Dataset, DataLoader
import torch
from tqdm import tqdm
import numpy as np



def cal_compressed(in_file, save_recode):
    tokenizer = AutoTokenizer.from_pretrained("pre_trained_model/Salesforce/codet5-small")
    data = load_json_file(in_file=in_file, return_dict=True)
    all_retio = []
    for i in data:
        input = i["question"]
        output = i["code"].strip()
        i_len = len(tokenizer(input)["input_ids"])
        o_len = len(tokenizer(output)["input_ids"])
        cr = o_len / i_len
        all_retio.append(cr)
        
    data = pd.DataFrame(all_retio, columns=['compressed_ratio'])
    data.to_csv(save_recode, index=False)


class Data_Encoder(Dataset):
    def __init__(self, file):
        # load data
        with open(file, 'r') as f:
            self.seqs = f.readlines()

    def __len__(self):
        """Denotes the total number of samples"""
        return len(self.seqs)

    def __getitem__(self, index):
        data = json.loads(self.seqs[index])
        return data 

def cal_gradient(save_recode, in_file=None):
    # data loader
    dataset = Data_Encoder(in_file)
    training_generator = DataLoader(dataset, batch_size=1, shuffle=False, num_workers=0)
    
    model = AutoModelForSeq2SeqLM.from_pretrained("/root/zhuxuekai/comparison_methods_of_HITL/pre_trained_model/Salesforce/codet5-small").cuda()
    tokenizer = AutoTokenizer.from_pretrained("/root/zhuxuekai/comparison_methods_of_HITL/pre_trained_model/Salesforce/codet5-base")
    # for key in model.state_dict().keys():
    #     print(key)
    model.train()
    gradients = []
    opt = torch.optim.Adam(model.parameters())
    for i, item in enumerate(tqdm(training_generator)):
        question = item["question"]
        code = item["code"]
        
        ids = tokenizer(question, return_tensors="pt")
        label = tokenizer(code, return_tensors="pt")
        
        outputs = model(input_ids=ids["input_ids"].cuda(), labels=label["input_ids"].cuda())
        loss = outputs.loss
        # logits = outputs.logits
        loss.backward()
        
        final_gradient = model.lm_head.weight.grad.clone().detach().cpu().numpy()
        l2_norm = np.linalg.norm(final_gradient, axis=0)
        norm_mean = np.mean(l2_norm)
        # gradients_batch = torch.autograd.grad(
        # loss, outputs.last_hidden_state,
        # grad_outputs = torch.ones_like(outputs.last_hidden_state), retain_graph = True, create_graph=True)[0][:, -1]

        gradients.append(norm_mean)
        opt.zero_grad()
        
    data = pd.DataFrame(gradients, columns=['gradient'])
    data.to_csv(save_recode, index=False)

def cal_entropy(save_recode, in_file=None):
    # data loader
    dataset = Data_Encoder(in_file)
    training_generator = DataLoader(dataset, batch_size=1, shuffle=False, num_workers=0)
    
    tokenizer = LlamaTokenizer.from_pretrained("/root/pubmodels/transformers/llama/llama-13b/tokenizer")
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})
    model = LlamaForCausalLM.from_pretrained("/root/pubmodels/transformers/llama/llama-13b/llama-13b").cuda()
    # for key in model.state_dict().keys():
    #     print(key)
    model.train()
    entropy = []
    for i, item in enumerate(tqdm(training_generator)):
        question = item["question"]
        code = item["code"]
        
        ids = tokenizer([question[0] + code[0], question[0]], return_tensors="pt", padding=True)
        # label = tokenizer(question + code, return_tensors="pt")
        inputs_ids = ids["input_ids"][0]
        labels = torch.where(ids["input_ids"][1] == inputs_ids, -100, ids["input_ids"][0])
        # print(labels)
        
        
        outputs = model(input_ids=inputs_ids.unsqueeze(0).cuda(), labels=labels.unsqueeze(0).cuda())
        loss = outputs.loss.clone().detach().cpu().numpy()
        # logits = outputs.logits
        # loss.backward()
        
        # final_gradient = model.lm_head.weight.grad.clone().detach().cpu().numpy()
        # gradients_batch = torch.autograd.grad(
        # loss, outputs.last_hidden_state,
        # grad_outputs = torch.ones_like(outputs.last_hidden_state), retain_graph = True, create_graph=True)[0][:, -1]

        entropy.append(loss)
        
    data = pd.DataFrame(entropy, columns=['entropy'])
    data.to_csv(save_recode, index=False)

    
if __name__ == '__main__':
    # compressed ratio
    in_file = "/root/zhuxuekai/comparison_methods_of_HITL/dataset/gsm8k-generat-data/enhanced_data/7_time_data/train-enhanced.json"
    save_recode = "compressed_code/results.csv"
    # cal_compressed(in_file, save_recode)

    # gradient
    cal_gradient("gradient_v2.csv", in_file=in_file)
    
    # entropy
    # cal_entropy("entropy.csv", in_file=in_file)
