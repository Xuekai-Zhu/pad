import json

def load_data(file, file_out):
    with open(file, "r") as f:
        data = f.readlines()
    new_data = []
    with open(file_out, "w") as f_out:
        for i in data:
            item = json.loads(i)
            a = item["A"]
            worker_answer = item["worker_answer"]
            sorting_feedback = {"sorting": "The answer '{}'' is better than '{}'. What's your answer?".format(worker_answer, a)}
            new_item = json.dumps(sorting_feedback)
            new_data.append(sorting_feedback)
            f_out.write(new_item + "\n")
            
if __name__ == '__main__':
    f_in = "dataset/mic/test_care/care_in_test_1000.json"
    f_out = "dataset/mic/test_care/care_in_test_sorting_examples.json"
    load_data(f_in, f_out)
    
