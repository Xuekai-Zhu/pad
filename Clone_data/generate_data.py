import json
import openai
from tqdm import tqdm
import time
import os

# Set up the API key / my key
# openai.api_key = "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"

# key from hua ermo
# openai.api_key = "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"

# key from jiang che
# openai.api_key = "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"

# key from my
openai.api_key = "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"

# example 1
# with open("in-conetx-example.text", "r") as f:
#     contex = f.read()
    
# example 2
with open("dataset/in-context-examples/in-context-example-3.txt", "r") as f:
    contex = f.read()

# generate train samples
with open("dataset/gsm8k/train.jsonl", "r") as f:
    all_data = f.readlines()
    all_data_len = len(all_data)

# generate test samples
# with open("dataset/gsm8k/test-delete-first-4.jsonl", "r") as f:
#     all_data = f.readlines()

# final_save = "dataset/第二次尝试_整合之后的/output_solution.json"
final_save = "dataset/opan-ai-api-train-生成数据-3/code-test.json"

for run_time in range(100):
    try:
        with open("output_solution.json", "w") as f_out:
            for i, data_i in enumerate(tqdm(all_data)):
                if os.path.exists(final_save):
                    with open(final_save, "r") as f_now:
                        data = f_now.readlines()
                        num = len(data)
                    if i <= num-1:
                        continue
                    time.sleep(20)
                else:
                    with open(final_save, "w") as ff:
                        print("create log file {}".format(final_save))
                # extract question    
                item = json.loads(data_i)
                question = item["question"]
                final_inputs = contex + "\n Question: " + question + "\n Solution:"
                # print(final_inputs)
                # query openai
                completion = openai.ChatCompletion.create(
                                model = "gpt-3.5-turbo",
                                messages=[{"role":"user", "content":final_inputs}]
                            )
                
                out_item = json.dumps(completion)
                f_out.write(out_item + "\n")
        
        rum_time_save = final_save.replace(".json", "_{}".format(run_time),) + ".json"

        # read output file 
        with open("output_solution.json", "r") as f:
                data_now = f.readlines()  
                
        # copy last time results
        with open(final_save, "r") as f_now:
                data = f_now.readlines()       
        
        # save to record file
        with open(rum_time_save, "w") as f:
                for n in all_out_put_data:
                    f.write(n)       
        break
    except:
            # copy last time results
            with open(final_save, "r") as f_now:
                    data = f_now.readlines()
                    
            # copy now time results
            rum_time_save = final_save.replace(".json", "_{}".format(run_time),) + ".json"
            with open("output_solution.json", "r") as f:
                data_now = f.readlines()
            all_out_put_data = data + data_now
            
            # save to record file
            with open(rum_time_save, "w") as f:
                for n in all_out_put_data:
                    f.write(n)    
            final_save = rum_time_save
            
    