train-fix-23.jsonl 是指去掉了第23条chatgpt回答不出来的问题。
gsm8k-code-solution-by-chatgpt-fix-23.json 是指根据train-fix-23.jsonl qury chatgpt的接口的生成结果。
train.json 是指将train-fix-23.jsonl和生成code solution合成到一个文件。
refine-train.json 是指去掉生成错误和语法错误的code solution，全部正确的训练集。