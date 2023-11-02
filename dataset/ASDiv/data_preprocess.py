import xml.etree.ElementTree as ET
import json
from tqdm import tqdm

# 读取XML文件并获取根元素
tree = ET.parse('dataset/ASDiv/ASDiv.xml')
root = tree.getroot()

# 初始化一个空列表，用于存储问题字典
problems = []

# 遍历XML文件中的所有问题
for problem in root.iter('Problem'):
    problem_dict = {
        'ID': problem.get('ID'),
        'Grade': problem.get('Grade'),
        'Source': problem.get('Source'),
        'Body': problem.find('Body').text,
        'Question': problem.find('Question').text,
        'Solution-Type': problem.find('Solution-Type').text,
        'Answer': problem.find('Answer').text,
        'Formula': problem.find('Formula').text,
    }
    problems.append(problem_dict)

# 将问题字典列表存储为JSON文件
with open('dataset/ASDiv/data.json', 'w') as f:
    json.dump(problems, f, indent=2)

with open('dataset/ASDiv/data.json', "r") as f:
    data = json.load(f)
    
save_file = 'dataset/ASDiv/data_refine.json'
with open(save_file, "w") as f_out:
    for i in tqdm(data):
        q = i["Body"] + i["Question"]
        try:
            a = i["Answer"].split()[0]
            a = int(a)
        except:
            print(a)
            continue
        equation = i["Formula"]
        item = json.dumps({
            "question":q,
            "num_answer":a,
            "equation":equation,
        })
        f_out.write(item + "\n")