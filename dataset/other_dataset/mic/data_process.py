import pandas as pd
import os
import json
from tqdm import tqdm

def save_file(f_in, f_out):
    with open(f_out, "w") as f:
        for i in f_in:
          f.write(i + "\n")  

data = pd.read_csv("baselines/mic/data_rot/MIC.csv")
save_path = "data/mic"

data_lens = data.shape[0]
headers = data.columns.tolist()

if os.path.exists(save_path):
    os.makedirs(save_path)

train_set = []
vaild_set = []
test_set = []


data_list = {
    "train":[],
    "dev":[],
    "test":[]}

for index, line in tqdm(data.iterrows()):
    item = {}
    set_type = line["split"]
    if set_type not in data_list.keys():
        continue
    for col in headers:
        item[col] = line[col]
    data_list[set_type].append(json.dumps(item))
    
    

save_file(data_list["train"], "mic_train.json")
save_file(data_list["dev"], "mic_dev.json")
save_file(data_list["test"], "mic_test.json")

    
    