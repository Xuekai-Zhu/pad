import json
from collections import Counter
import os
from eval_code_solution import load_json_file
from tqdm import tqdm
import eventlet

def load_y(file):
    with open(file, "r") as f:
        all_data = f.readlines()
    return [json.loads(i) for i in all_data]

def load_fine_tune_y(file):
    all_data_list = []
    with open(file, "r") as f:
        all_data = f.readlines()
        for i in all_data:
            data = json.loads(i)
            out = data["output"].split("####")[-1]
            all_data_list.append(out)
    return all_data_list


def check_answer(predictions, golden_file):
    predict = load_y(predictions)
    golden = load_y(golden_file)
    right = 0
    for i,j in zip(predict, golden):
        p = i["output"]
        y = j["target"]
        if p in y or y in p:
            right += 1
    
    acc = right / len(golden)
    print("Accuracy: {}".format(acc))
    save_file = predictions.replace("generated_predictions.json", "result.eval")
    with open(save_file, "w") as f:
        f.write("Accuracy: {}".format(acc))

def check_answer_for_fine_tune(predictions, golden_file):
    predict = load_fine_tune_y(predictions)
    golden = load_y(golden_file)
    right = 0
    for i,j in zip(predict, golden):
        # p = i["output"]
        p = i
        y = j["target"]
        if p in y or y in p:
            right += 1
    
    acc = right / len(golden)
    print("Accuracy: {}".format(acc))
    save_file = predictions.replace("generated_predictions.json", "result.eval")
    with open(save_file, "w") as f:
        f.write("Accuracy: {}".format(acc))
    
    
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
            # if isinstance(y["num_answer"], str):
            #     answer = int(y["num_answer"].replace(',',''))
            # else:
            answer = y["target"]
                
            
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
                "answer":answer,
                })
            except:
                tmp = "Time Out"
                out_item = json.dumps({
                "output":tmp,
                "answer":answer,
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
                # y_predict = float(output)
                # y_predict = round(y_predict)
                # y_predict_round = round(output)
                # y = int(result["answer"])
                # if y_predict - y == 0:
                if output in result["answer"] or result["answer"] in output:
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
    
if __name__ == '__main__':
    # baselines 
    gloden_file = "dataset/BIG-Bench-Hard-main/bbh_processed/bbh.json"
    prediction = "model/code-t5-large/baseline-standard-GSM8K-tuning/bbh/generated_predictions.json"
    
    # other baselines
    # check_answer(prediction, gloden_file)
    
    # standard fine-tune
    # check_answer_for_fine_tune(prediction, gloden_file)
    
    # ours 
    result_dir = "model/code-t5-large/self_distillation/code-t5-large-lr-6e-5-distillation"
    test_file = result_dir + "/bbh-chain-verifying/" + "generated_predictions.json"
    gloden_file = "dataset/BIG-Bench-Hard-main/bbh_processed/bbh.json"
    save_dir = result_dir + "/bbh-chain-verifying/" + "test_code_python"
    test_code_solution_for_predict(test_file=test_file, golden_file=gloden_file, save_dir=save_dir)
    
    result_file = save_dir + "/" + "results.txt"
    calculate_acc(result_file)
    
    
