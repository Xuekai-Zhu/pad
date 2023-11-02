import json
from tqdm import tqdm

original_data = "dataset/SVAMP/SVAMP.json"

with open(original_data, "r") as f:
    data = json.load(f)
    
save_file = "dataset/SVAMP/svamp_refine.json"
with open(save_file, "w") as f_out:
    for i in tqdm(data):
        q = i["Body"] + " " + i["Question"]
        a = i["Answer"]
        equation = i["Equation"]
        item = json.dumps({
            "question":q,
            "num_answer":a,
            "equation":equation,
        })
        f_out.write(item + "\n")
        
