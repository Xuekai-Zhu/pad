import pandas as pd
import os
import json
import numpy as np

def load_data(in_file):
    with open(in_file, "r") as f:
        data = f.readlines()
        return [i for i in data]

in_file = "metric/results_for_enhanced_data/fathiful.tsv"
df = pd.read_csv(in_file, sep="\t")
filter_key = df.keys()[0]
fathful_list = np.array(df[[filter_key]])

print("Median:", np.median(fathful_list))
print("Mean:", np.mean(fathful_list))

data_in_dir = ["dataset/gsm8k-generat-data/gsm8k-1/train_file/refine-train-delete-question.json", 
               "dataset/gsm8k-generat-data/gsm8k-2/refine-train-delete-question.json",
               "dataset/gsm8k-generat-data/gsm8k-3/refine-train-delete-question.json",
               "dataset/gsm8k-generat-data/gsm8k-4/refine-train-delete-question.json",
               "dataset/gsm8k-generat-data/gsm8k-5/refine-train.json",
               "dataset/gsm8k-generat-data/gsm8k-6/refine-train.json",
               "dataset/gsm8k-generat-data/gsm8k-7/refine-train.json",
               "dataset/gsm8k-generat-data/gsm8k-8/refine-train.json",
               ]

all_data = []
for i in data_in_dir:
    datas = load_data(i)
    all_data.extend(datas)


all_filter_data_8 = []
all_filter_data_7764 = []
for i, score in zip(all_data, fathful_list):
    if score >= 0.8:
        all_filter_data_8.append(i)
    if score >= 0.7764:
        all_filter_data_7764.append(i)

with open("dataset/gsm8k-generat-data/enhanced_data/filter_data/0.8_train.json", "w") as f_out:
    for i in all_filter_data_8:
        f_out.write(i)
        
with open("dataset/gsm8k-generat-data/enhanced_data/filter_data/0.7764_train.json", "w") as f_out:
    for i in all_filter_data_7764:
        f_out.write(i)