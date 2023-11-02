import json
import openai
from tqdm import tqdm
import time
import os


# key for 5美元
openai.api_key = "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"
openai.organization = "org-4otMUxXRoM3AgyvTssYvNam4"


# completion = openai.ChatCompletion.create(
#   model="gpt-4",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Hello!"}
#   ]
# )

# print(completion.choices[0].message)
    
# example 2
with open("../Clone_data/dataset/in-context-examples/in-conetx-example-1.text", "r") as f:
    contex = f.read()

# generate train samples
with open("../Clone_data/dataset/gsm8k/train.jsonl", "r") as f:
    all_data = f.readlines()
    all_data_len = len(all_data)

# generate test samples
# with open("dataset/gsm8k/test-delete-first-4.jsonl", "r") as f:
#     all_data = f.readlines()

# final_save = "dataset/第二次尝试_整合之后的/output_solution.json"
final_save = "clone_pad_from_code_davinci_002/pad_data.json"
run_time_file = "output_pad_c.json"

for run_time in range(20):
    # try:
        with open(run_time_file, "w") as f_out:
            for i, data_i in enumerate(tqdm(all_data)):
                if os.path.exists(final_save):
                    with open(final_save, "r") as f_now:
                        data = f_now.readlines()
                        num = len(data)
                    if i <= num-1:
                        continue
                    # time.sleep(20)
                else:
                    with open(final_save, "w") as ff:
                        print("create log file {}".format(final_save))
                # extract question    
                item = json.loads(data_i)
                question = item["question"]
                final_inputs = contex + "\n Question: " + question + "\n Solution:"
                # print(final_inputs)
                # query openai
                # completion = openai.ChatCompletion.create(
                #                 # model = "gpt-3.5-turbo",
                #                 model = "text-davinci-002",
                #                 messages=[{"role":"user", "content":final_inputs}]
                #             )
                completion = openai.Completion.create(
                    # engine="text-davinci-002",
                    engine="code-davinci-002",
                    prompt=final_inputs,
                    max_tokens=256
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
        all_out_put_data = data + data_now
        with open(rum_time_save, "w") as f:
                for n in all_out_put_data:
                    f.write(n)       
        break
            
    # except:
    #     # copy last time results
    #     with open(final_save, "r") as f_now:
    #             data = f_now.readlines()
                
    #     # copy now time results
    #     rum_time_save = final_save.replace(".json", "_{}".format(run_time),) + ".json"
    #     with open(run_time_file, "r") as f:
    #         data_now = f.readlines()
    #     all_out_put_data = data + data_now
        
    #     # save to record file
    #     with open(rum_time_save, "w") as f:
    #         for n in all_out_put_data:
    #             f.write(n)    
    #     final_save = rum_time_save
    
    