from transformers import OPTConfig, OPTModel, GPT2Tokenizer, OPTForCausalLM
from data_preprocess import Data_Preprocess
from torch.utils.data import DataLoader
import torch
from tqdm import tqdm
import json


def write_to_file(output, file):
    for i in output:
        item = {
                "output":i,
            }
        str_item = json.dumps(item)
        file.write(str_item + "\n")

def load_showing_examples(file):
    showing_list = []
    with open(file, "r") as f:
        data = f.readlines()
        
    for i in data:
        item = json.loads(i)
        showing = item["showing"]
        showing_list.append(showing)
        
    return showing_list

def load_sorting_examples(file):
    sorting_list = []
    with open(file, "r") as f:
        data = f.readlines()
        
    for i in data:
        item = json.loads(i)
        sorting = item["sorting"]
        sorting_list.append(sorting)
        
    return sorting_list
    
    
    
    

def mic_dialogue(tokenizer, model, out_file, data_generator, 
                 use_rot=False, 
                 use_showing=False, showing_files=None, 
                 use_categorizing=False,
                 use_sorting=False,
                 sorting_file=None,
                 ):
    if use_showing:
        examples = load_showing_examples(showing_files)
    elif use_sorting:
        examples = load_sorting_examples(sorting_file)
    
    with open(out_file, "w") as f_in:
        for i, (q, a, rot, work_answer) in enumerate(tqdm(data_generator)):
            if use_rot:
                q = [n + " " + m for n,m in zip(q, rot)]
            elif use_showing:
                showing_examples = examples[i*len(q):(i+1)*(len(q))]
                q = [n + " " + m for n,m in zip(showing_examples, q)]
            elif use_sorting:
                sorting_examples = examples[i*len(q):(i+1)*(len(q))]
                q = [n + " " + m for n,m in zip(q, sorting_examples)]
                
            inputs = tokenizer(q, padding=True, return_tensors="pt").to(device)
            generate_ids = model.generate(inputs.input_ids, max_new_tokens=64, do_sample=False)
            output_withpast = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)
            output = [i.replace(j, "", 1).strip() for i,j in zip(output_withpast, q)]
            write_to_file(output, f_in)
            # print(output)
            

if __name__ == '__main__':
    # config
    device = torch.device('cuda' if True and torch.cuda.is_available() else 'cpu')
    tokenizer = GPT2Tokenizer.from_pretrained("pre_trained_model/facebook/opt-2.7b", padding_side='left')
    model = OPTForCausalLM.from_pretrained("pre_trained_model/facebook/opt-2.7b").to(device)


    # data
    file = "dataset/mic/test_care/care_in_test_1000.json"
    dataset = Data_Preprocess(file)
    data_generator = DataLoader(dataset, batch_size=4, shuffle=False, num_workers=0)
    
    
    # run dialogue
    
    # # w/o Rot
    # out_file = "./predict/opt-2.7b/care_1000_test/base.json"
    # mic_dialogue(tokenizer, model, out_file, data_generator)
    
    # # evaluating
    # out_file = "./predict/opt-2.7b/care_1000_test/base+rot.json"
    # mic_dialogue(tokenizer, model, out_file, data_generator, use_rot=True)
    
    # # showing
    # out_file = "./predict/opt-2.7b/care_1000_test/base+showing.json"
    # mic_dialogue(tokenizer, model, out_file, data_generator, use_showing=True, 
    #              showing_files="dataset/mic/test_care/care_in_test_showing_examples.json")
    
    # sorting
    out_file = "./predict/opt-2.7b/care_1000_test/base+sorting.json"
    mic_dialogue(tokenizer, model, out_file, data_generator, use_sorting=True, 
                 sorting_file="dataset/mic/test_care/care_in_test_sorting_examples.json")
