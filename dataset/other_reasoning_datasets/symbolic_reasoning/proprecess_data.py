import json
import random

def read_data(in_file):
    with open(in_file, "r") as f:
        data_dict = json.load(f)
    data = data_dict['data']
    return data

def save_data(in_data, save_file):
    with open(save_file, "w") as f_out:
        for i in in_data:
            new_item = {
                "question":i["question"],
                "answer":i["answer"],
            }
            new_item = json.dumps(new_item)
            f_out.write(new_item + "\n")
def divide_into_test(in_file, save_dir):
    with open(in_file, "r") as f:
        data = f.readlines()
    
    random.shuffle(data)
    elements_count = int(len(data) * 0.7)
    train = data[:elements_count]
    test = data[elements_count:]
    with open(save_dir + "/train.json", "w") as f:
        for i in train:
            f.write(i)
            
    with open(save_dir + "/test.json", "w") as f:
        for i in test:
            f.write(i)
            
    
    
        
if __name__ == '__main__':
    # coin_flip
    # in_data = "dataset/other_reasoning_datasets/symbolic_reasoning/orignal_data/coin_flip.json"
    # data = read_data(in_data)
    # save_data(data, in_data.replace(".json", "-refine.json"))
    
    # # last_letter_concatenation
    # in_data = "dataset/other_reasoning_datasets/symbolic_reasoning/orignal_data/last_letter_concatenation.json"
    # data = read_data(in_data)
    # save_data(data, in_data.replace(".json", "-refine.json"))
    
    # divide 
    # in_file = "dataset/other_reasoning_datasets/symbolic_reasoning/coin_filp/coin_filp_code_refine.json"
    # save_dir = "dataset/other_reasoning_datasets/symbolic_reasoning/coin_filp"
    # divide_into_test(in_file, save_dir)
    
    # in_file = "dataset/other_reasoning_datasets/symbolic_reasoning/las_letter_concat/last_letter_concat_code_refine.json"
    # save_dir = "dataset/other_reasoning_datasets/symbolic_reasoning/las_letter_concat"
    # divide_into_test(in_file, save_dir)
    
    in_file = "dataset/other_reasoning_datasets/commense_qa/strategy_qa/strategy_qa_code_refine.json"
    save_dir = "dataset/other_reasoning_datasets/commense_qa/strategy_qa/"
    divide_into_test(in_file, save_dir)