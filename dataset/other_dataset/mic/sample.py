import random
import json


with open("dataset/mic/test_care/care_in_test.json", "r") as f:
    data = f.readlines()

sample_1000 = data[:1000]
rest_sample = data[1000:]

with open("dataset/mic/test_care/care_in_test_1000.json", "w") as f_out:
    for i in sample_1000:
        f_out.write(i)
        
        
with open("dataset/mic/test_care/care_in_test_rest.json", "w") as f_out:
    for i in rest_sample:
        f_out.write(i)