from transformers import AutoModel
import torch
from tqdm import tqdm




model_1_dir = "model/model_for_merge/code-t5-samll-enhanced-7time-learning-4e-5"
model_2_dir = "model/model_for_merge/code-t5-samll-enhanced-7time-learning-5e-5"
model_3_dir = "model/model_for_merge/code-t5-samll-enhanced-7time-learning-6e-5"

# 加载模型
model_1 = AutoModel.from_pretrained(model_1_dir)
model_2 = AutoModel.from_pretrained(model_2_dir)
model_3 = AutoModel.from_pretrained(model_3_dir)


# 创建一个新模型，用于存储平均后的权重
model_avg = AutoModel.from_pretrained(model_1_dir)

# 初始化权重之和
state_dict_avg = {}
for key in model_1.state_dict().keys():
    state_dict_avg[key] = torch.zeros_like(model_1.state_dict()[key])

# 累加权重
for model in [model_1, model_2, model_3]:
    for key in model.state_dict().keys():
        state_dict_avg[key] += model.state_dict()[key]

# 计算平均权重
for key in tqdm(state_dict_avg.keys()):
    state_dict_avg[key] /= 3

# 将新的平均权重加载到新模型中
model_avg.load_state_dict(state_dict_avg)

# save 
save_dir = "model/model_for_merge/meger_model_from_4e-5_and_5e-5_and_6e-5"
model_avg.save_pretrained(save_dir)



