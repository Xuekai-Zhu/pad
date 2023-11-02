import json
import os


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
            out = data["output"]
            all_data_list.append(out)
    return all_data_list
            
def calculate_solve_rate(f_gold, f_test, llama=False, decoder_model=False):
    golden = load_num_answer(f_gold)
    predict = load_predict(f_test)
    
    all_data_num = len(golden)
    right_answer = 0
    if llama:
        for i, j in zip(golden, predict):
            answer = str(i["answer"])

            j = j.replace(i["input"], "")
            # j = j.split()[0]
            if answer in j or j in answer or answer.replace(".0", "") in j:
                
                right_answer += 1
    else:
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
    
    # gsm8k
    # golden_test_file = "dataset/gsm8k-generat-data/gsm8k-1/test_file/test_add_code.json"
    # in_put_dir = "baelines_predict/gsm8k/chatglm-6b"
    # predict_file = in_put_dir + "/generated_predictions.json"
    # calculate_solve_rate(golden_test_file, predict_file, llama=True)
    
    # # ASDiv
    golden_test_file = "dataset/ASDiv/data_refine.json"
    in_put_dir = "model/code-t5-small/code-t5-samll-enhanced-7time-learning-6e-5/ASDiv-chain-verifying"
    predict_file = in_put_dir + "/generated_predictions.json"
    # calculate_solve_rate(golden_test_file, predict_file, llama=True)
    calculate_solve_rate(golden_test_file, predict_file)
    
    # SVAMP
    # golden_test_file = "dataset/SVAMP/svamp_refine.json"
    # in_put_dir = "baelines_predict/SVAMP/llama-13b"
    # predict_file = in_put_dir + "/generated_predictions.json"
    # calculate_solve_rate(golden_test_file, predict_file, llama=True, decoder_model=True)
    
    # Mathi Arith
    # golden_test_file = "dataset/MultiArith/multi_arith_refine.json"
    # in_put_dir = "baelines_predict/MultiArith/llama-13b"
    # predict_file = in_put_dir + "/generated_predictions.json"
    # calculate_solve_rate(golden_test_file, predict_file, llama=True)
    
    # predict_file_add_solution = "predict/opt-1.3b/gsm8k-add_solution-{}/results.txt"
    # for i in range(run_time):
    #     calculate_solve_rate(golden_test_file, predict_file_add_solution.format(i))
    
    # # instruction
    # predict_file_iml = "predict/opt-iml-1.3b/gsm8k-{}/results.txt"
    # for i in range(run_time):
    #     calculate_solve_rate(golden_test_file, predict_file_iml.format(i))
        
    # predict_file_iml_add_solution = "predict/opt-iml-1.3b/gsm8k-add_solution-{}/results.txt"
    # for i in range(run_time):
    #     calculate_solve_rate(golden_test_file, predict_file_iml_add_solution.format(i))
    