import json

def load_answer(file):
    all_data_list = []
    with open(file, "r") as f:
        all_data = f.readlines()
        for i in all_data:
            data = json.loads(i)
            solution, answer = data["answer"].split("####")
            inputs_dict = {
                "input":data["question"],
                "solution":solution.strip(),
                "answer":answer.strip(),
            }
            all_data_list.append(inputs_dict)
            
    return all_data_list


def load_num_answer(file):
    all_data_list = []
    with open(file, "r") as f:
        all_data = f.readlines()
        for i in all_data:
            data = json.loads(i)
            answer = data["num_answer"]
            if isinstance(answer, str):
                try:
                    answer = float(answer.strip())
                except:
                    answer = float(answer.replace(",", "").strip())
            inputs_dict = {
                "input":data["question"],
                # "solution":solution.strip(),
                "answer":answer,
            }
            all_data_list.append(inputs_dict)
            
    return all_data_list


def load_predict(file):
    all_data_list = []
    with open(file, "r") as f:
        all_data = f.readlines()
        for i in all_data:
            data = json.loads(i)
            out = data["output"].split("####")[-1]
            all_data_list.append(out)
    return all_data_list

            
def calculate_solve_rate(f_gold, f_test):
    golden = load_num_answer(f_gold)
    predict = load_predict(f_test)
    
    all_data_num = len(golden)
    right_answer = 0
    for i, j in zip(golden, predict):
            try:
                j = float(j)
                if i["answer"] == float(j):
                    right_answer += 1
            except:
                continue
    result =  right_answer / all_data_num
    log_info = "All Data: {}; Answer Right: {}; Solve Rate: {}".format(all_data_num, right_answer, result)
    print(log_info)
    save_file = f_test.replace("generated_predictions.json", "solve_rate.txt")
    with open(save_file, "w") as f:
        f.write(log_info)
    
    

if __name__ == '__main__':
    # GSM8K
    # golden_test_file = "dataset/gsm8k-generat-data/gsm8k-1/test_file/test_add_code.json"
    # in_put_dir = "model/code-t5-large/baseline-standard-GSM8K-tuning"
    # predict_file = in_put_dir + "/generated_predictions.json"
    # calculate_solve_rate(golden_test_file, predict_file)
    
    
    
    # ASDiv
    # golden_test_file = "dataset/ASDiv/data_refine.json"
    # in_put_dir = "model/code-t5-large/baseline-standard-GSM8K-tuning/ASDiv"
    # predict_file = in_put_dir + "/generated_predictions.json"
    # calculate_solve_rate(golden_test_file, predict_file)
    
    # SVAMP
    # golden_test_file = "dataset/SVAMP/svamp_refine.json"
    # in_put_dir = "model/code-t5-large/baseline-standard-GSM8K-tuning/SVAMP"
    # predict_file = in_put_dir + "/generated_predictions.json"
    # calculate_solve_rate(golden_test_file, predict_file)
    
    # Mathi Arith
    golden_test_file = "dataset/MultiArith/multi_arith_refine.json"
    in_put_dir = "model/code-t5-large/baseline-standard-GSM8K-tuning/MultiArith"
    predict_file = in_put_dir + "/generated_predictions.json"
    calculate_solve_rate(golden_test_file, predict_file)