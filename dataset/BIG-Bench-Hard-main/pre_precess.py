import json
import os


def load_sorce_file(in_file):
    with open(in_file, "r") as f:
        lines = f.readlines()[0]
        data = json.loads(lines)
    task = in_file.split("/")[-1].replace(".json", "")
    datas = data["examples"]
    for i in datas:
        i["task"]=task
    return datas
# 指定文件夹路径
folder_path = "dataset/BIG-Bench-Hard-main/bbh"

# 用于存储文件名的列表
file_names = []

# 使用walk函数遍历文件夹中的每个文件
for root, dirs, files in os.walk(folder_path):
    for file in files:
        # 将文件名和路径合并，得到完整的文件路径
        file_path = os.path.join(root, file)
        # 将完整的文件路径添加到列表中
        if file_path.endswith(".json"):
            file_names.append(file_path)
        
out_path_file = "dataset/BIG-Bench-Hard-main/bbh_processed/bbh.json"
all_data = []

for i in file_names:
    data_list = load_sorce_file(i)
    all_data.extend(data_list)



with open(out_path_file, "w") as f:
    for i in all_data:
        new_item = {
            "question":i["input"],
            "target":i["target"],
            "task":i["task"],
        }
        new_item = json.dumps(new_item)
        f.write(new_item + "\n")