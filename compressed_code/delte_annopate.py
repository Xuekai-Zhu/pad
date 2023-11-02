import json
from transformers import AutoTokenizer
import csv
import re
from tqdm import tqdm
import os
import eventlet

def remove_comments(code):
    
    return re.sub(r'#.*$', '', code, flags=re.MULTILINE)


def load_json_file(in_file, return_dict=False):
    with open(in_file, "r") as f:
        data = f.readlines()
    if return_dict:
        all_data = [json.loads(i) for i in data]
        return all_data
    else:
        return data
    
    
def delte_annatote(in_file, save_file):
    data = load_json_file(in_file, return_dict=True)
    with open(save_file, "w") as f_out:
        for i in tqdm(data):
            code = i["code"]
            re_code = remove_comments(code)
            i["code"] = re_code
            
            save_item = json.dumps(i)
            f_out.write(save_item + "\n")


def delte_first_last(in_file, save_file):
    data = load_json_file(in_file, return_dict=True)
    with open(save_file, "w") as f_out:
        for i in tqdm(data):
            code = i["code"]
            re_code = code.replace("def solution():\n", "")
            re_code = re_code.replace("return result", "")
            i["code"] = re_code
            
            save_item = json.dumps(i)
            f_out.write(save_item + "\n")
    
    
    
    
    
def check_code(test_file=None, save_dir=None):
    data = load_json_file(test_file, return_dict=True)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        
    for i, item in enumerate(tqdm(data)):
        code = item["code"]
        python_file = os.path.join(save_dir, "{}.py".format(i))
        with open(python_file, "w") as f_py:
            f_py.write(code + "\n\nprint(solution())")
        # try:
        eventlet.monkey_patch()
            # with eventlet.Timeout(30):
        tmp = os.popen('python {}'.format(python_file)).readlines()
                # out_item = json.dumps({
                # "output":tmp,
                # "answer":str(answer),
                # })
            # except:
            #     tmp = "Time Out"
            #     out_item = json.dumps({
            #     "output":tmp,
            #     "answer":str(answer),
            #     }) 
    
        
        
            
# test case             
# code = """def solution():\n    # Calculate the height of each stack\n    stack1 = 7\n    stack2 = stack1 + 3\n    stack3 = stack2 - 6 # Calculate the height of each stack\n    stack4 = stack3 + 10\n\n    # Calculate the total number of blocks used\n    total_blocks = stack1 + stack2 + stack3 + stack4 + (2 * stack2)\n\n    result = total_blocks\n    return result"""
# clean_code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)
# print(clean_code)

if __name__ == '__main__':
    in_file = "dataset/gsm8k-generat-data/enhanced_data/7_time_data/train-enhanced.json"
    save_file = "dataset/gsm8k-generat-data/enhanced_data/7_time_data/train-enhanced-cleaned-annotation.json"
    # delte_annatote(in_file, save_file)
    save_file_2 = "dataset/gsm8k-generat-data/enhanced_data/7_time_data/train-enhanced-cleaned-annotation-more.json"
    delte_first_last(save_file, save_file_2)
    
    # check code
    # check_code(save_file, "compressed_code/test_code")
    