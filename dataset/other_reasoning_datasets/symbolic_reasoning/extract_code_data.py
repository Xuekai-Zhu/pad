import json
from tqdm import tqdm
import os
import eventlet

def load_json_file(in_file, return_dict=False):
    with open(in_file, "r") as f:
        data = f.readlines()
    if return_dict:
        all_data = [json.loads(i) for i in data]
        return all_data
    else:
        return data
    
def extract_results(in_file):
    with open(in_file, "r") as f_in:
        input_data = f_in.readlines()
        input_dict = [json.loads(i) for i in input_data]
        
    save_file = in_file.replace("gpt-3.5-test", "answers")
    with open(save_file, "w") as f_out:
        for i in input_dict:
            solution = i["choices"][0]["message"]["content"]
            item = json.dumps(
                {"output":solution}
            )
            f_out.write(item + "\n")




def merge_data(data_file, solution_file, save_file):
    source_data = load_json_file(data_file, return_dict=True)
    solution_data = load_json_file(solution_file, return_dict=True)
    # tokenizer = AutoTokenizer.from_pretrained("pre_trained_model/Salesforce/codet5-large")
    # check the lenght
    assert len(source_data) == len(solution_data)
    with open(save_file, "w") as f_out:
        for i,j in zip(source_data, solution_data):
            solution = j["choices"][0]["message"]["content"]
            if not solution.startswith("def solution():"):
                continue
            new_item = {
                "question": i["question"],
                "code": solution,
                "answer": i["answer"]
            }
            save_item = json.dumps(new_item)
            f_out.write(save_item + "\n")
            
    print("merge data done !!!!!!!!!!!!!")

def filter_bad_code(in_file, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    source_data = load_json_file(in_file, return_dict=True)
    results_file = os.path.join(save_dir, "results.txt")
    py_sricpt_output = []
    for i, j in enumerate(source_data):
        code = j["code"]
        answer = j["answer"].lower()
        
        # save intermediate code
        python_file = os.path.join(save_dir, "{}.py".format(i))
        with open(python_file, "w") as f_py:
            f_py.write(code + "\n\nprint(solution())")
        try:
            eventlet.monkey_patch()
            with eventlet.Timeout(30):
                tmp = os.popen('python {}'.format(python_file)).readlines()
            out_item = json.dumps({
            "output":tmp,
            "answer":str(answer),
            })
        except:
                tmp = "Time Out"
                out_item = json.dumps({
                "output":tmp,
                "answer":str(answer),
                })    
        py_sricpt_output.append(out_item)    
            
        with open(results_file, "w") as f_out:
            for i in py_sricpt_output:
                f_out.write(i + "\n")

def calculate_acc(results_file, if_save=False, save_file=None, source_data=None):
    out_file = results_file.replace(".txt", ".eval")
    index_file = results_file.replace(".txt", ".index")
    with open(results_file, "r") as f_in:
        data = f_in.readlines()
    num = len(data)
    empty = 0
    right = 0
    output_wrong = 0
    right_index = []
    # right_data = []
    for i, j in enumerate(data):
        result = json.loads(j)
        output = result["output"]
        if len(output) < 1:
            empty += 1
            continue
        output = output[0].strip()
        try:
            y_predict = output.lower()
            # y_predict = round(y_predict)
            # y_predict_round = round(output)
            y = result["answer"].lower()
            if y_predict == y:
                right += 1
                right_index.append(i)
                # right_data.append(j)
        except:
            # empty += 1
            output_wrong += 1
    
    correct_code = 1 - empty/num
    acc = right/num
    
    print("generate syntactically correct code: {}".format(correct_code))
    print("Accuracy: {}".format(acc))
    with open(out_file, "w") as f_out:
        f_out.write("generate syntactically correct code: {}".format(correct_code) + "\n" + "Accuracy: {}".format(acc))
    with open(index_file, "w") as f_out:
        for i in right_index:
            f_out.write(str(i) + "\n")
    if if_save:
        save_right_index(right_index, save_file, source_data)
    
def save_right_index(right_index, save_file, orignal_file):
    with open(orignal_file, "r") as f:
        data = f.readlines()
    refine_data = [data[i] for i in right_index]
    with open(save_file, "w") as f:
        for i in refine_data:
            f.write(i)
    print("save finish")
    
    
    

if __name__ == '__main__':
    # coin flip
    # in_file = "Clone_data/clone_other_reasoning_data/coin_flip/gpt-reponse-code.json"
    # f_gold = "dataset/other_reasoning_datasets/symbolic_reasoning/orignal_data/coin_flip-refine.json"
    # save_1 = "dataset/other_reasoning_datasets/symbolic_reasoning/orignal_data/coin_flip_add_code.json"
    # merge_data(f_gold, in_file, save_1)
    
    # test code
    # code_save_dir = "dataset/other_reasoning_datasets/commense_qa/coin_filp" + "/test_code"
    # filter_bad_code(save_1, save_dir)
    
    # filter
    # save_dir = "dataset/other_reasoning_datasets/symbolic_reasoning/coin_filp"
    # results_file = save_dir + "/test_code/results.txt"
    # save_file = save_dir + "/" + "coin_filp_code_refine.json"
    # calculate_acc(results_file, if_save=True, save_file=save_file, source_data=save_1)
    
    # late letter concatenation
    # in_file = "Clone_data/clone_other_reasoning_data/last_letter_concate/gpt-reponse-code.json"
    # f_gold = "dataset/other_reasoning_datasets/symbolic_reasoning/orignal_data/last_letter_concatenation-refine.json"
    # save_1 = f_gold.replace("last_letter_concatenation-refine.json", "last_letter_concatenation-refine-add-code.json")
    # merge_data(f_gold, in_file, save_1) 

    # # test code
    # code_save_dir = "dataset/other_reasoning_datasets/symbolic_reasoning/las_letter_concat" + "/test_code"
    # filter_bad_code(save_1, code_save_dir)
    # # filter
    # save_dir = "dataset/other_reasoning_datasets/symbolic_reasoning/las_letter_concat"
    # results_file = save_dir + "/test_code/results.txt"
    # save_file = save_dir + "/" + "last_letter_concat_code_refine.json"
    # calculate_acc(results_file, if_save=True, save_file=save_file, source_data=save_1)
    
    
    # strage qa
    # in_file = "Clone_data/clone_other_reasoning_data/strategy_qa/gpt-reponse-code.json"
    # f_gold = "dataset/other_reasoning_datasets/commense_qa/orignnal_data/strategy_qa-refine.json"
    # save_1 = f_gold.replace("strategy_qa-refine.json", "strategy_qa-refine-add-code.json")
    # merge_data(f_gold, in_file, save_1) 
    
    # # test code
    # code_save_dir = "dataset/other_reasoning_datasets/commense_qa/strategy_qa" + "/test_code"
    # filter_bad_code(save_1, code_save_dir)
    
    # # filter
    # save_dir = "dataset/other_reasoning_datasets/commense_qa/strategy_qa"
    # results_file = save_dir + "/test_code/results.txt"
    # save_file = save_dir + "/" + "strategy_qa_code_refine.json"
    # calculate_acc(results_file, if_save=True, save_file=save_file, source_data=save_1)