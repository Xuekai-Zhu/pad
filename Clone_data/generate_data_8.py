import json
import openai
from tqdm import tqdm
import time
import os

# Set up the API key / my key
# openai.api_key = "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"

# my key from gmail
# openai.api_key = "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"

# my key from 1436127191@qq.com
# openai.api_key = "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"

# key from hua ermo
# openai.api_key = "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"

# key from jiang che
# openai.api_key = "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"

# key for 5美元
openai.api_key = "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"

# example 1
# with open("in-conetx-example.text", "r") as f:
#     contex = f.read()
    
# example 2
with open("dataset/in-context-examples/in-context-example-8.txt", "r") as f:
    contex = f.read()

# generate train samples
with open("dataset/gsm8k/train.jsonl", "r") as f:
    all_data = f.readlines()
    all_data_len = len(all_data)

# generate test samples
# with open("dataset/gsm8k/test-delete-first-4.jsonl", "r") as f:
#     all_data = f.readlines()


final_save = "dataset/openai-api-train-生成数据-8/code_contest.json"
run_time_file = "output_solution-8.json"

for run_time in range(100):
    try:
        with open(run_time_file, "w") as f_out:
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
                # add input
                completion["input"] = question
                completion["answer"] = item["answer"]
                
                out_item = json.dumps(completion)
                f_out.write(out_item + "\n")
                
        rum_time_save = final_save.replace(".json", "_{}".format(run_time),) + ".json"

        # read output file 
        with open(run_time_file, "r") as f:
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
        with open(run_time_file, "r") as f:
            data_now = f.readlines()
        all_out_put_data = data + data_now
        
        # save to record file
        with open(rum_time_save, "w") as f:
            for n in all_out_put_data:
                f.write(n)    
        final_save = rum_time_save
    
    