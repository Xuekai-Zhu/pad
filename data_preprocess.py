from torch.utils.data import Dataset, DataLoader
import os
import json
import torch
import pickle
import random
from transformers import default_data_collator
from tqdm import tqdm
from nltk import sent_tokenize
from datasets import load_dataset
from random import random

# MIC dataset and preprocess code

class MIC_Data_Preprocess(Dataset):

    def __init__(self, file):
        # load data
        with open(file, 'r') as f:
            self.lines = f.readlines()

    def __len__(self):
        """Denotes the total number of samples"""
        return len(self.lines)

    def __getitem__(self, index):
        data = json.loads(self.lines[index])
        q = data['Q'].strip()
        a = data["A"].strip()
        rot = data["rot"].strip()
        work_answer = data["worker_answer"].strip()
        # QA = data["worker_answer"].strip()

        return q, a, rot, work_answer
    
def check_mic_dataset():
    # load mic
    file = "dataset/mic/mic_test.json"
    dataset = MIC_Data_Preprocess(file)
    data_generator = DataLoader(dataset, batch_size=1, shuffle=False, num_workers=0)
    for i, (q, a, rot, work_answer) in enumerate(data_generator):
        print(q)
        print(a)
        print(rot)
        print(work_answer)
        print('----------------------------------------------------')
    
    
# instruction tuning dataset preprocess code
class NI_DataFunction(Dataset):
    def __init__(self, file):
        # load data
        with open(file, 'r') as f:
            self.lines = f.readlines()

    def __len__(self):
        """Denotes the total number of samples"""
        return len(self.lines)

    def __getitem__(self, index):
        data = json.loads(self.lines[index])
        return data
    
def check_ni_dataset():
    file = "dataset/natural-instruction-v2-json/tokenized_text/tokenized_validation.json"
    # file = "test.json"
    dataset = NI_DataFunction(file)
    data_generator = DataLoader(dataset, 
                                batch_size=32, 
                                shuffle=False, 
                                collate_fn=default_data_collator
                                )
    for step, batch in enumerate(tqdm(data_generator)):
        # batch = {k: v.cuda() for k, v in batch.items()}
        print("----------  {}   ------------".format(step))
        print(torch.sum(batch["labels"] == -100))
        print(batch["labels"].size())
        # if batch["labels"].size()[-1] >= 1020:
        #     print(step)
        #     break
        
def check_len_ni_dataset():
    tokenized_file_in = ["dataset/natural-instruction-v2-json/tokenized_text/tokenized_{}.json".format(i) for i in ["train", "validation", "test"]]
    tokenized_num = []
    for file_i in tokenized_file_in:
        with open(file_i, "r") as f:
            lines = f.readlines()
            tokenized_num.append(len(lines))
        len_list = []
        for i in tqdm(lines):
            data = json.loads(i)
            input_ids = data["input_ids"]
            now_len = len(input_ids)
            if now_len not in len_list:
                len_list.append(now_len)
                
        print(len_list)
        print("-----------------------")
    print(tokenized_num)
    
    
    file_in = ["dataset/natural-instruction-v2-json/text/{}.json".format(i) for i in ["train", "validation", "test"]]
    num = []
    for file_i in file_in:
        with open(file_i, "r") as f:
            lines = f.readlines()
            num.append(len(lines))
    print("-----------------------")           
    print(num)
    print("-----------------------")
        
# GSM8K dataset and preprocess code

class GSM8K_DataFunction(Dataset):
    def __init__(self, file):
        # load data
        with open(file, 'r') as f:
            self.lines = f.readlines()

    def __len__(self):
        """Denotes the total number of samples"""
        return len(self.lines)

    def __getitem__(self, index):
        data = json.loads(self.lines[index])
        solution, answer = data["answer"].split("####")
        inputs_dict = {
            "input":data["question"],
            "solution":solution.strip(),
            "answer":answer.strip(),
        }
        return inputs_dict
    
def check_gsm8k_dataset():
    file = "dataset/grade-school-math/grade_school_math/data/test.jsonl"
    # file = "test.json"
    dataset = GSM8K_DataFunction(file)
    data_generator = DataLoader(dataset, 
                                batch_size=1, 
                                shuffle=False, 
                                # collate_fn=default_data_collator
                                )
    for step, batch in enumerate(tqdm(data_generator)):
        print("---------- {} ------------".format(step))
        print(batch)
        print(batch.keys())
        # print(batch["labels"].size())
        break

def add_solution_to_question(f_in, f_out):
    new_data = []
    with open(f_in, "r") as f:
        all_data = f.readlines()
        for i in all_data:
            data = json.loads(i)
            solution, answer = data["answer"].split("####")
            sentens = sent_tokenize(data["question"])
            sentens.insert(len(sentens)-1 , solution.strip())
            inputs_dict = {
                "input":" ".join(sentens),
                # "solution":solution.strip(),
                "answer":answer.strip(),
            }
            new_data.append(inputs_dict)
            
    with open(f_out, "w") as f_out:
        for i in tqdm(new_data):
            item = json.dumps(i)
            f_out.write(item + "\n")
            
class GSM8K_Add_Solution_DataFunction(Dataset):
    def __init__(self, file):
        # load data
        with open(file, 'r') as f:
            self.lines = f.readlines()

    def __len__(self):
        """Denotes the total number of samples"""
        return len(self.lines)

    def __getitem__(self, index):
        data = json.loads(self.lines[index])
        answer = data["answer"]
        inputs_dict = {
            "input":data["input"],
            # "solution":solution.strip(),
            "answer":answer,
        }
        return inputs_dict
    
    
    
class PAL_dataset(Dataset):

    def __init__(self, file):
        # load data
        with open(file, 'r') as f:
            self.lines = f.readlines()

    def __len__(self):
        """Denotes the total number of samples"""
        return len(self.lines)

    def __getitem__(self, index):
        data = json.loads(self.lines[index])
        question = data["input"]
        code = data["code"]
        target = data["target"]
        return data
    
def check_pal_dataset():
    file = "baselines/pal/datasets/gsmhardv2.jsonl"
    dataset = PAL_dataset(file)
    data_generator = DataLoader(dataset, 
                                batch_size=1, 
                                shuffle=False, 
                                # collate_fn=default_data_collator
                                )
    for step, batch in enumerate(tqdm(data_generator)):
        print("---------- {} ------------".format(step))
        print(batch["input"])
        print("--"*9)
        print(batch["code"])
        print("--"*9)
        print(batch["target"])
        print("--"*9)
        # print(batch)
        print(batch.keys())
        # print(batch["labels"].size())
        break
    
def check_pal_from_dataset_modul():
    file = "baselines/pal/datasets/gsmhardv2.jsonl"
    data = load_dataset(file)
    print("---------")


def extract_pal_val_data(val, train, all):
    file = "baselines/pal/datasets/gsmhardv2.jsonl"
    with open(file, "r") as f_in:
        data = f_in.readlines()
    num = int(len(data) * 0.95)
    train_data = data[:num]
    val_data = data[num:]
    with open(all, "w") as f:
        for i in data:
            f.write(i)
    with open(val, "w") as f:
        for i in val_data:
            f.write(i)
            
    with open(train, "w") as f:
        for i in train_data:
            f.write(i)


# preprocess code solution data

def load_json_file(in_file, return_dict=False):
    with open(in_file, "r") as f:
        data = f.readlines()
    if return_dict:
        all_data = [json.loads(i) for i in data]
        return all_data
    else:
        return data

def merge_data(data_file, solution_file, save_file):
    source_data = load_json_file(data_file, return_dict=True)
    solution_data = load_json_file(solution_file, return_dict=True)
    assert len(source_data) == len(solution_data)
    with open(save_file, "w") as f_out:
        for i,j in zip(source_data, solution_data):
            solution = j["choices"][0]["message"]["content"]
            question = i["question"]
            # try:
            #     assert question in solution
            # except:
            #     print(question)
            #     print("---------------------")
            #     print(solution)
            #     # break
    
            i["code"] = solution.strip()
            num_answer = i["answer"].split("####")[-1].strip()
            i["num_answer"] = num_answer
            save_item = json.dumps(i)
            f_out.write(save_item + "\n")
            
    print("pre-process done !!!!!!!!!!!!!")

def extract_right_train_data():
    index_file = "dataset/gsm8k-0306/train_code_python/results.index"
    train_file = "dataset/gsm8k-0306/train.json"
    refine_train_file = "dataset/gsm8k-0306/refine-train.json"
    with open(index_file, "r") as f_in:
        index_list = f_in.readlines()
        index_list = [int(i) for i in index_list]
        
    with open(train_file, "r") as f:
        data = f.readlines()
        
    with open(refine_train_file, "w") as f_out:
        for i in index_list:
            f_out.write(data[i])
        
def extract_right_test_data():
    index_file = "dataset/gsm8k-0306/test_file/test_code_python/results.index"
    test_file = "dataset/gsm8k-0306/test_file/test_add_code.json"
    refine_train_file = "dataset/gsm8k-0306/test_file/refine-test_add_code.json"
    with open(index_file, "r") as f_in:
        index_list = f_in.readlines()
        index_list = [int(i) for i in index_list]
        
    with open(test_file, "r") as f:
        data = f.readlines()
        
    with open(refine_train_file, "w") as f_out:
        for i in index_list:
            f_out.write(data[i])
    
    
    

if __name__ == '__main__':
    # load mic
    # check_mic_dataset()
        
    # load NI
    # check_ni_dataset()
    # check_len_ni_dataset()
    
    # load gsma8k
    # check_gsm8k_dataset()
    
    # insert solution to questions
    # add_solution_to_question("dataset/grade-school-math/grade_school_math/data/test.jsonl", 
    #                          "dataset/grade-school-math/grade_school_math/data/test_add_solution.jsonl")
    
    # load PAL dataset
    # check_pal_dataset()
    # check_pal_from_dataset_modul()
    
    # extratc PAL val \train
    # extract_pal_val_data("dataset/PAL_data/val.json", "dataset/PAL_data/train.json", "dataset/PAL_data/all.json")
    
    # merge openai generate code solution for gsm8k 
    # merge_data("dataset/gsm8k-0306/train-fix-23.jsonl", "dataset/gsm8k-0306/gsm8k-code-solution-by-chatgpt-fix-23.json", "dataset/gsm8k-0306/train.json")
    merge_data("dataset/gsm8k-0306/test_file/test_delete_first_four.jsonl", "dataset/gsm8k-0306/test_file/code-test.json", "dataset/gsm8k-0306/test_file/test_add_code.json")
    
    # extract right code training data
    # extract_right_train_data()
    # extract_right_test_data()