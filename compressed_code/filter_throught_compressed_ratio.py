import pandas as pd
import json
import numpy as np


def load_json_file(in_file, return_dict=False):
    with open(in_file, "r") as f:
        data = f.readlines()
    if return_dict:
        all_data = [json.loads(i) for i in data]
        return all_data
    else:
        return data

# save index
com_ratio = pd.read_csv("compressed_code/results_compressed_ratio.csv")
data = load_json_file("dataset/gsm8k-generat-data/enhanced_data/7_time_data/train-enhanced.json")
df_data = pd.DataFrame(data, columns=['data'])

merge_df = pd.concat([com_ratio, df_data], axis=1)
merge_df = merge_df.reset_index()

sorted_df = merge_df.sort_values(by='compressed_ratio')

# sorted_df.to_csv("dataset/gsm8k-generat-data/enhanced_data/filter_data/compress_retio/sorted_data.csv")

save_dir = "dataset/gsm8k-generat-data/enhanced_data/filter_data/compress_v2"

def save_to_json(ratio, sorted_df, save_dir):
    save_file = save_dir + "{}_compressed.json".format(ratio)
    n = int(ratio * len(sorted_df))
    top_n = sorted_df["data"].iloc[0:n].to_list()
    with open(save_file, "w") as f:
        for i in top_n:
            f.write(i)

save_to_json(0.1, sorted_df, save_dir)
save_to_json(0.2, sorted_df, save_dir)
save_to_json(0.3, sorted_df, save_dir)
save_to_json(0.4, sorted_df, save_dir)
save_to_json(0.5, sorted_df, save_dir)
save_to_json(0.6, sorted_df, save_dir)
save_to_json(0.7, sorted_df, save_dir)
save_to_json(0.8, sorted_df, save_dir)
save_to_json(0.9, sorted_df, save_dir)

# data = top_n["data"].to_list()
# print(top_n[0])



