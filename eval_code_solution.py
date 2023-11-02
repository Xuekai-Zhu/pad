import json
from tqdm import tqdm
import os
import subprocess
import eventlet

def load_json_file(in_file, return_dict=False):
    with open(in_file, "r") as f:
        data = f.readlines()
    if return_dict:
        all_data = [json.loads(i) for i in data]
        return all_data
    else:
        return data

def test_code_solution(test_file, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    results_file = os.path.join(save_dir, "results.txt")

    data = load_json_file(test_file, return_dict=True)
    py_sricpt_output = []
    with open(results_file, "w") as f_out:
        for i, item in enumerate(tqdm(data)):
            code = item["code"]
            answer = int(item["num_answer"].replace(',',''))
            
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

        
def calculate_acc(results_file):
    out_file = results_file.replace(".txt", ".eval")
    index_file = results_file.replace(".txt", ".index")
    with open(results_file, "r") as f_in:
        data = f_in.readlines()
    num = len(data)
    empty = 0
    right = 0
    output_wrong = 0
    right_index = []
    for i, j in enumerate(data):
        result = json.loads(j)
        output = result["output"]
        if len(output) == 1:
            output = output[0].strip()
            try:
                y_predict = float(output)
                y_predict = round(y_predict)
                # y_predict_round = round(output)
                y = int(result["answer"])
                if y_predict - y == 0:
                    
                    right += 1
                    right_index.append(i)
                # else:
                #     print(result)
            except:
                # empty += 1
                output_wrong += 1
        else:
            empty += 1
    
    correct_code = 1 - empty/num
    acc = right/num
    
    print("generate syntactically correct code: {}".format(correct_code))
    print("Accuracy: {}".format(acc))
    with open(out_file, "w") as f_out:
        f_out.write("generate syntactically correct code: {}".format(correct_code) + "\n" + "Accuracy: {}".format(acc))
    with open(index_file, "w") as f_out:
        for i in right_index:
            f_out.write(str(i) + "\n")
    
def test_code_solution_for_predict(test_file=None, golden_file=None, save_dir=None):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        
    results_file = os.path.join(save_dir, "results.txt")

    data = load_json_file(test_file, return_dict=True)
    golden_data = load_json_file(golden_file, return_dict=True)
    py_sricpt_output = []
    with open(results_file, "w") as f_out:
        for i, (item, y) in enumerate(tqdm(zip(data, golden_data))):
            code = item["output"]
            if isinstance(y["num_answer"], str):
                answer = int(y["num_answer"].replace(',',''))
            else:
                answer = int(y["num_answer"])
                
            
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

    
if __name__ == '__main__':
    # test open ai output on train file of gsm8k
    # test_code_solution("dataset/gsm8k-generat-data/gsm8k-0313/train_add_code.json", save_dir="dataset/gsm8k-generat-data/gsm8k-0313/output_python_code")   
   
    # calculate_acc("dataset/gsm8k-0306/train_file/train_code_python/results.txt")
    # calculate_acc("dataset/gsm8k-generat-data/gsm8k-0313/output_python_code/results.txt")
    
    # test open ai output on train file of gsm8k
    # input_file = "rebuttal_clone_data/clone_pad_data_from_text-davinci-002/test/refine-train-davinci-002-delete-question.json"
    # save_file = "rebuttal_clone_data/clone_pad_data_from_text-davinci-002/test/test_code_python"
    # test_code_solution(input_file, save_file)   
    # result_file = save_file + "/" + "results.txt"
    # calculate_acc(result_file)
    
    # our fine-tune model
    # gsm8k
    # result_dir = "model/one-time-data/codet5-large"
    # test_file = result_dir + "/" + "generated_predictions.json"
    # gloden_file = "dataset/gsm8k-generat-data/gsm8k-1/test_file/test_add_code.json"
    # save_dir = result_dir + "/" + "test_code_python"
    # test_code_solution_for_predict(test_file=test_file, golden_file=gloden_file, save_dir=save_dir)
    
    # result_file = save_dir + "/" + "results.txt"
    # calculate_acc(result_file)
    
    # ASDiv
    # result_dir = "model/code-t5-large/self_distillation/code-t5-large-lr-6e-5-distillation"
    # test_file = result_dir + "/ASDiv-chain-verifying/" + "generated_predictions.json"
    # gloden_file = "dataset/ASDiv/data_refine.json"
    # save_dir = result_dir + "/ASDiv-chain-verifying/" + "test_code_python"
    # test_code_solution_for_predict(test_file=test_file, golden_file=gloden_file, save_dir=save_dir)
    
    # result_file = save_dir + "/" + "results.txt"
    # calculate_acc(result_file)
    
    # SVAMP
    # result_dir = "model/one-time-data/codet5-small"
    # test_file = result_dir + "/SVAMP/" + "generated_predictions.json"
    # gloden_file = "dataset/SVAMP/svamp_refine.json"
    # save_dir = result_dir + "/SVAMP/" + "test_code_python"
    # test_code_solution_for_predict(test_file=test_file, golden_file=gloden_file, save_dir=save_dir)
    
    # result_file = save_dir + "/" + "results.txt"
    # calculate_acc(result_file)
    
    # MultiArith
    result_dir = "model/one-time-data/codet5-small"
    test_file = result_dir + "/MultiArith/" + "generated_predictions.json"
    gloden_file = "dataset/MultiArith/multi_arith_refine.json"
    save_dir = result_dir + "/MultiArith/" + "test_code_python"
    test_code_solution_for_predict(test_file=test_file, golden_file=gloden_file, save_dir=save_dir)
    
    result_file = save_dir + "/" + "results.txt"
    calculate_acc(result_file)