import json


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
            
  
def load_predict(file):
    all_data_list = []
    with open(file, "r") as f:
        all_data = f.readlines()
        for i in all_data:
            data = json.loads(i)
            out = data["output"]
            all_data_list.append(out)
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
  
            
def calculate_solve_rate(f_gold, f_test):
    golden = load_num_answer(f_gold)
    predict = load_predict(f_test)
    
    all_data_num = len(golden)
    right_answer = 0
    for i, j in zip(golden, predict):
        ans = i["answer"]
        try:
            j = float(j)
            if ans == float(j):
                right_answer += 1
        except:
            if isinstance(j, str):
                if str(ans) in j:
                    right_answer += 1

    result =  right_answer / all_data_num
    log_info = "All Data: {}; Answer Right: {}; Solve Rate: {}".format(all_data_num, right_answer, result)
    print(log_info)
    save_file = f_test.replace("answers.json", "solve_rate.txt")
    with open(save_file, "w") as f:
        f.write(log_info)
        
        
if __name__ == '__main__':
    # ASDiv
    # in_file = "Clone_data/test-for-chatgpt/ASDiv/gpt-3.5-test.json"
    # f_gold = "dataset/ASDiv/data_refine.json"
    # extract_results(in_file)
    # calculate_solve_rate(f_gold, in_file.replace("gpt-3.5-test", "answers"))
    
    # SVAMP
    # in_file = "Clone_data/test-for-chatgpt/SVAMP/gpt-3.5-test.json"
    # f_gold = "dataset/SVAMP/svamp_refine.json"
    # extract_results(in_file)
    # calculate_solve_rate(f_gold, in_file.replace("gpt-3.5-test", "answers"))
    
    # MA
    in_file = "Clone_data/test-for-chatgpt/MultiArith/gpt-3.5-test.json"
    f_gold = "dataset/MultiArith/multi_arith_refine.json"
    extract_results(in_file)
    calculate_solve_rate(f_gold, in_file.replace("gpt-3.5-test", "answers"))