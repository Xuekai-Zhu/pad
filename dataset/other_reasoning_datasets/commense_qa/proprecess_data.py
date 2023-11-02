import json
import random

def read_data(in_file):
    with open(in_file, "r") as f:
        data_dict = json.load(f)
    data = data_dict['data']
    return data

def save_data(in_data, save_file, type=None):
    with open(save_file, "w") as f_out:
        for i in in_data:
            if type is not None:
                new_item = {
                "question":i["rationale"] + " " + i["question"],
                "answer":i["answer"],
            }
            else:
                new_item = {
                    "question":i["question"],
                    "answer":i["answer"],
                }
            new_item = json.dumps(new_item)
            f_out.write(new_item + "\n")

        
if __name__ == '__main__':
    # commonsense_qa
    in_data = "dataset/other_reasoning_datasets/commense_qa/orignnal_data/commonsense_qa.json"
    data = read_data(in_data)
    # data = random.sample(data, 1221)
    save_data(data, in_data.replace(".json", "-refine.json"))
    
    # strategy_qa
    in_data = "dataset/other_reasoning_datasets/commense_qa/orignnal_data/strategy_qa.json"
    data = read_data(in_data)
    # data = random.sample(data, 687)
    save_data(data, in_data.replace(".json", "-refine.json"), type="strageqa")