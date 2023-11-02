import json
from tqdm import tqdm

test_file = "dataset/mic/mic_test.json"


# with open(test_file, "r") as f:
#     data = f.readlines()
    
# care_list = []
# need_att = "care"
# for i in data:
#     item = json.loads(i)
#     att = item["moral"]
#     if isinstance(att, str) and need_att in att:
#         care_list.append(i)
        
# with open("care_in_test.json", "w") as f_out:
#     for i in tqdm(care_list):
#         f_out.write(i)
        
# showing list

def load_showing_examples(file):
    showing_list = []
    with open(file, "r") as f:
        data = f.readlines()
        
    for i in data:
        item = json.loads(i)
        showing = "You can learn from an example. {} {} Then answer the following the question.".format(item["Q"].strip(), item["worker_answer"].strip())
        showing_item = json.dumps({
            "showing": showing,
        })
        showing_list.append(showing_item)
        
    return showing_list

showing_file = "dataset/mic/test_care/care_in_test_rest.json"

showing_list = load_showing_examples(showing_file)

with open("dataset/mic/test_care/care_in_test_showing_examples.json", "w") as f:
    for i in showing_list:
        f.write(i + "\n")