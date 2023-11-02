import json
from tqdm import tqdm
import os
from nltk import sent_tokenize
import re

def load_json_file(in_file, return_dict=False):
    with open(in_file, "r") as f:
        data = f.readlines()
    if return_dict:
        all_data = [json.loads(i) for i in data]
        return all_data
    else:
        return data
    
    
def test_code_solution_for_predict(test_file=None, golden_file=None, results_file=None):
    
    data = load_json_file(test_file, return_dict=True)
    golden_data = load_json_file(golden_file, return_dict=True)
    
    right = 0
    all_num = len(data)
    with open(results_file, "w") as f_out:
        for i, (item, y) in enumerate(tqdm(zip(data, golden_data))):
            cot = item["output"]
            if isinstance(y["num_answer"], str):
                answer = int(y["num_answer"].replace(',',''))
            else:
                answer = int(y["num_answer"])
                

            pattern = r'Answer: ([\S]+)'
            match = re.search(pattern, cot)
            if match:
                final_answer = match.group(1)
            else:
                sens = sent_tokenize(cot)
                final_answer = sens[-1]
            if str(answer) in final_answer:
                right += 1

    acc = right/all_num
    print("Accuracy: {}".format(acc))
    with open(results_file, "w") as f_out:
        f_out.write("Accuracy: {}".format(acc))

                
if __name__ == '__main__':
    # gsm8k
    # result_dir = "model/3.5-turbo/codet5-large"
    # test_file = result_dir + "/" + "generated_predictions.json"
    # gloden_file = "dataset/gsm8k-generat-data/gsm8k-1/test_file/test_add_code.json"
    # result_file = save_dir + "/" + "results.txt"
    # test_code_solution_for_predict(test_file=test_file, golden_file=gloden_file, results_file=result_file)
    
    # SVAMP
    # result_dir = "model/3.5-turbo/codet5-small"
    # test_file = result_dir + "/SVAMP/" + "generated_predictions.json"
    # gloden_file = "dataset/SVAMP/svamp_refine.json"
    # result_file = result_dir + "/" + "SVAMP_results.txt"
    # test_code_solution_for_predict(test_file=test_file, golden_file=gloden_file, results_file=result_file)
    
    # MultiArith
    result_dir = "model/3.5-turbo/codet5-large"
    test_file = result_dir + "/MultiArith/" + "generated_predictions.json"
    gloden_file = "dataset/MultiArith/multi_arith_refine.json"
    result_file = result_dir + "/" + "MultiArith_results.txt"
    test_code_solution_for_predict(test_file=test_file, golden_file=gloden_file, results_file=result_file)
    