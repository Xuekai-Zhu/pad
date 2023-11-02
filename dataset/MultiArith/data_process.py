import json
from tqdm import tqdm

original_data = "dataset/MultiArith/MultiArith.json"

with open(original_data, "r") as f:
    data = json.load(f)
    
save_file = "dataset/MultiArith/multi_arith_refine.json"
with open(save_file, "w") as f_out:
    for i in tqdm(data):
        q = i["sQuestion"]
        a = i["lSolutions"]
        assert len(a) == 1
        
        equation = i["lEquations"]
        item = json.dumps({
            "question":q,
            "num_answer":a[0],
            "equation":equation,
        })
        f_out.write(item + "\n")