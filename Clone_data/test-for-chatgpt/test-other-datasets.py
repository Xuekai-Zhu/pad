import json
import openai
from tqdm import tqdm
import time
import os

# Set up the API key / my key
openai.api_key = "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"


# prompt = "You should provide answer to the following question without any other contents."
prompt = "Please provide numerical answers only and do not include any other text in your response."

# input dataset
# ASDiv dataset/ASDiv/data_refine.json
in_file = "/root/zhuxuekai/comparison_methods_of_HITL/dataset/ASDiv/data_refine.json"
final_save = "./ASDiv/gpt-3.5-test.json"


# SVAMP
in_file = "/root/zhuxuekai/comparison_methods_of_HITL/dataset/SVAMP/svamp_refine.json"
final_save = "./SVAMP/gpt-3.5-test.json"

# MA
in_file = "/root/zhuxuekai/comparison_methods_of_HITL/dataset/MultiArith/multi_arith_refine.json"
final_save = "./MultiArith/gpt-3.5-test.json"


with open(in_file, "r") as f:
    input_data = f.readlines()
    # all_data = [json.loads(i) for i in input_data]


for run_time in range(100):
    try:
        with open("output_solution.json", "w") as f_out:
            for i, data_i in enumerate(tqdm(input_data)):
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
                final_inputs = prompt + " Question: " + question + "\n Answer:"
                # print(final_inputs)
                # query openai
                completion = openai.ChatCompletion.create(
                                model = "gpt-3.5-turbo",
                                messages=[{"role":"user", "content":final_inputs}]
                            )
                completion["input_question"] = question
                out_item = json.dumps(completion)
                f_out.write(out_item + "\n")
        
        
        rum_time_save = final_save.replace(".json", "_{}".format(run_time),) + ".json"

        # # read output file 
        with open("output_solution.json", "r") as f:
                data_now = f.readlines()  
                
        # # copy last time results
        with open(final_save, "r") as f_now:
                data_previous = f_now.readlines()       
        
        all_out_put_data = data_previous + data_now
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
            
    