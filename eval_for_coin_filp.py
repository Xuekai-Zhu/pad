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
    
def test_code_solution_for_predict(test_file=None, golden_file=None, save_dir=None):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        
    results_file = os.path.join(save_dir, "results.txt")

    data = load_json_file(test_file, return_dict=True)
    golden_data = load_json_file(golden_file, return_dict=True)
    py_sricpt_output = []
    
    for i, (item, y) in enumerate(tqdm(zip(data, golden_data))):
        code = item["output"]
        answer = y["answer"].lower()
        
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
            
if __name__ == '__main__':
    # coin filp
    # result_dir = "model/coin_filp/code-t5-large/6e-5"
    # test_file = result_dir + "/" + "generated_predictions.json"
    # gloden_file = "dataset/other_reasoning_datasets/symbolic_reasoning/coin_filp/test.json"
    # save_dir = result_dir + "/" + "test_code_python"
    # test_code_solution_for_predict(test_file=test_file, golden_file=gloden_file, save_dir=save_dir)
    
    # result_file = save_dir + "/" + "results.txt"
    # calculate_acc(result_file)


    # last letter concat
    # result_dir = "model/last_letter/code-t5-large/6e-5"
    # test_file = result_dir + "/" + "generated_predictions.json"
    # gloden_file = "dataset/other_reasoning_datasets/symbolic_reasoning/las_letter_concat/test.json"
    # save_dir = result_dir + "/" + "test_code_python"
    # test_code_solution_for_predict(test_file=test_file, golden_file=gloden_file, save_dir=save_dir)
    
    # result_file = save_dir + "/" + "results.txt"
    # calculate_acc(result_file)
    
    # strategy qa
    result_dir = "model/strategy_qa/code-t5-large/6e-5"
    test_file = result_dir + "/" + "generated_predictions.json"
    gloden_file = "dataset/other_reasoning_datasets/commense_qa/strategy_qa/test.json"
    save_dir = result_dir + "/" + "test_code_python"
    test_code_solution_for_predict(test_file=test_file, golden_file=gloden_file, save_dir=save_dir)
    
    result_file = save_dir + "/" + "results.txt"
    calculate_acc(result_file)
