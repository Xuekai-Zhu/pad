import json
from transformers import AutoTokenizer
import csv
import re
from tqdm import tqdm
import os

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
    tokenizer = AutoTokenizer.from_pretrained("pre_trained_model/Salesforce/codet5-large")
    # check the lenght
    assert len(source_data) == len(solution_data)
    with open(save_file, "w") as f_out:
        for i,j in zip(source_data, solution_data):
            if "message" in j["choices"][0]:
                solution = j["choices"][0]["message"]["content"]
            else:
                solution = j["choices"][0]["text"]
            if "Sorry, as an AI language model, I cannot provide a solution in this case as there are some crucial details missing." in solution:
                continue
            
            question = i["question"]
            # check question corresponding to solution
            try:
                q_tokens = tokenizer(question)["input_ids"]
                s_tokens = tokenizer(solution)["input_ids"]
                assert len(q_tokens) == len(s_tokens)
            except:
                print(question)
                print("---------------------")
                print(solution)
                # break
    
            i["code"] = solution.strip()
            num_answer = i["answer"].split("####")[-1].strip()
            i["num_answer"] = num_answer
            save_item = json.dumps(i)
            f_out.write(save_item + "\n")
            
    print("pre-process done !!!!!!!!!!!!!")

def statics_code_length(file_in, save_out):
    
    data = load_json_file(file_in, return_dict=True)
    tokenizer = AutoTokenizer.from_pretrained("pre_trained_model/Salesforce/codet5-large")
    len_list = []
    for i in data:
        solution = i["code"]
        question = i["question"]
        code_len = tokenizer(solution)["input_ids"]
        q_len = tokenizer(question)["input_ids"]
        len_list.append([len(q_len), len(code_len)])
    
    with open(save_out, 'w', newline='') as f:
         # 创建csv writer对象
        writer = csv.writer(f)
        writer.writerow(["inputs_length", "code_length"])
        # 将列表数据写入csv文件
        for row in len_list:
            writer.writerow(row)
         
def extract_right_train_data(index_file=None, data_file=None, refine_data_file=None):
    # index_file = "dataset/gsm8k-0306/train_code_python/results.index"
    # train_file = "dataset/gsm8k-0306/train.json"
    # refine_train_file = "dataset/gsm8k-0306/refine-train.json"
    with open(index_file, "r") as f_in:
        index_list = f_in.readlines()
        index_list = [int(i) for i in index_list]
        
    with open(data_file, "r") as f:
        data = f.readlines()
        
    with open(refine_data_file, "w") as f_out:
        for i in index_list:
            f_out.write(data[i])

def delete_question_in_code(in_file, out_file):
    data = load_json_file(in_file, return_dict=True)
    with open(out_file, "w") as f:
        for i in tqdm(data):
            code = i["code"]
            # print(code)
            code_without_question = re.sub(r'"""[^"]*"""', '', code)
            print(code_without_question)
            i["code"] = code_without_question
            new_item = json.dumps(i)
            f.write(new_item + "\n")
    
def meger_data_for_enhaced(in_file_list, out_file):
    all_data = []
    for i_file in in_file_list:
        i_data = load_json_file(i_file)
        all_data.extend(i_data)
        
    with open(out_file, "w") as f_in:
        for i in all_data:
            f_in.write(i)


if __name__ == '__main__':
    # merge data
    source_file = "dataset/grade-school-math/grade_school_math/data/train.jsonl"
    chatgpt_output = "rebuttal_clone_data/clone_CoT_data/cot_data_0.json"
    merge_data(source_file, chatgpt_output, "rebuttal_clone_data/clone_CoT_data/train_add_cot_data_gpt-3.5.json")
    
    # check data length
    # save_out = "dataset/gsm8k-generat-data/enhanced_data/7_time_data/" + "code_length.csv"
    # statics_code_length("dataset/gsm8k-generat-data/enhanced_data/7_time_data/train-enhanced.json", "code_length.csv")
    # statics_code_length("dataset/gsm8k-generat-data/gsm8k-0313/refine-train-delete-question.json", "code_length.csv")
    
    # extract_right_train_data
    # data_dir = "rebuttal_clone_data/clone_pad_data_from_text-davinci-002"
    # index_file = os.path.join(data_dir, "test_code_python/results.index") 
    # data_file = os.path.join(data_dir, "train_add_code_davinci-002.json")
    # refine_data_file = os.path.join(data_dir, "refine-train_davinci-002.json")
    # extract_right_train_data(index_file=index_file, data_file=data_file, refine_data_file=refine_data_file)
    
    # delete question in code
    # in_dir = "rebuttal_clone_data/clone_pad_data_from_text-davinci-002"
    # in_file = os.path.join(in_dir, "refine-train_davinci-002.json")
    # out_file = os.path.join(in_dir, "refine-train-davinci-002-delete-question.json")
    # delete_question_in_code(in_file, out_file)
    
    # in_file = "dataset/gsm8k-generat-data/gsm8k-0306/train_file/refine-train.json"
    # out_file = "dataset/gsm8k-generat-data/gsm8k-0306/train_file/refine-train-delete-question.json"
    # delete_question_in_code(in_file, out_file)


    # merge data for enhance
    # 1 time file
    # input_file_list = ["dataset/gsm8k-generat-data/gsm8k-0313/refine-train-delete-question.json", "dataset/gsm8k-generat-data/gsm8k-0306/train_file/refine-train-delete-question.json"]
    # save_file = "dataset/gsm8k-generat-data/enhanced_data/train-enhanced.json"
    
    # # 2 time file 
    # input_file_list = ["dataset/gsm8k-generat-data/enhanced_data/1_time_data/train-enhanced.json", "dataset/gsm8k-generat-data/gsm8k-3/refine-train-delete-question.json"]
    # save_file = "dataset/gsm8k-generat-data/enhanced_data/2_time_data/train-enhanced.json"
    
    # # 3 time file
    # input_file_list = ["dataset/gsm8k-generat-data/enhanced_data/2_time_data/train-enhanced.json", "dataset/gsm8k-generat-data/gsm8k-4/refine-train-delete-question.json"]
    # save_file = "dataset/gsm8k-generat-data/enhanced_data/3_time_data/train-enhanced.json"
    
    # # 4 time file
    # input_file_list = ["dataset/gsm8k-generat-data/enhanced_data/3_time_data/train-enhanced.json", "dataset/gsm8k-generat-data/gsm8k-5/refine-train.json"]
    # save_file = "dataset/gsm8k-generat-data/enhanced_data/4_time_data/train-enhanced.json"
    
    # # # # 5 time file
    # input_file_list = ["dataset/gsm8k-generat-data/enhanced_data/4_time_data/train-enhanced.json", "dataset/gsm8k-generat-data/gsm8k-6/refine-train.json"]
    # save_file = "dataset/gsm8k-generat-data/enhanced_data/5_time_data/train-enhanced.json"
    
    # # 6 time file
    # input_file_list = ["dataset/gsm8k-generat-data/enhanced_data/5_time_data/train-enhanced.json", "dataset/gsm8k-generat-data/gsm8k-7/refine-train.json"]
    # save_file = "dataset/gsm8k-generat-data/enhanced_data/6_time_data/train-enhanced.json"
    
    # # 7 time file
    # input_file_list = ["dataset/gsm8k-generat-data/enhanced_data/6_time_data/train-enhanced.json", "dataset/gsm8k-generat-data/gsm8k-8/refine-train.json"]
    # save_file = "dataset/gsm8k-generat-data/enhanced_data/7_time_data/train-enhanced.json"
    
    
    # meger_data_for_enhaced(input_file_list, save_file)