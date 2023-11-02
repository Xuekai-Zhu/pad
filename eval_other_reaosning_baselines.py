import json
# from tqdm import tqdm

def load_json_file(in_file, return_dict=False):
    with open(in_file, "r") as f:
        data = f.readlines()
    if return_dict:
        all_data = [json.loads(i) for i in data]
        return all_data
    else:
        return data
    
    
def calculate_acc(results_file, golden_file):
    out_file = results_file.replace(".json", ".eval")
    predictions = load_json_file(results_file, return_dict=True)
    predictions = [i["output"].strip().lower() for i in predictions]
    y = load_json_file(golden_file, return_dict=True)
    y = [j["answer"].lower() for j in y]
    num = len(predictions)
    right = 0
    for n,m in zip(predictions, y):
        if n == m:
            right += 1
            
    # correct_code = 1 - empty/num
    acc = right/num
    
    # print("generate syntactically correct code: {}".format(correct_code))
    print("Accuracy: {}".format(acc))
    with open(out_file, "w") as f_out:
        f_out.write("Accuracy: {}".format(acc))
    # with open(index_file, "w") as f_out:
    #     for i in right_index:
    #         f_out.write(str(i) + "\n")

if __name__ == '__main__':
    # coin_filp
    prediction = "model/code-t5-large/baseline-standard-coin_filp-tuning/generated_predictions.json"
    gloden_file = "dataset/other_reasoning_datasets/symbolic_reasoning/coin_filp/test.json"
    # calculate_acc(prediction, gloden_file)
    
    # 
    # prediction = "model/code-t5-large/baseline-standard-last_letter-tuning/generated_predictions.json"
    # gloden_file = "dataset/other_reasoning_datasets/symbolic_reasoning/las_letter_concat/test.json"
    # calculate_acc(prediction, gloden_file)
    
    # strategy qa
    prediction = "model/code-t5-large/baseline-standard-strategy_qa-tuning/generated_predictions.json"
    gloden_file = "dataset/other_reasoning_datasets/commense_qa/strategy_qa/test.json"
    calculate_acc(prediction, gloden_file)