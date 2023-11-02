code-test.jsonl 生成code的结果
train_add_code.json 是将生成code加到训练集中去。
refine-train.json 是指去掉生成错误和语法错误的code solution，全部正确的训练集。
refine-train-delete-question.json 是删除code中的 “question”之后的。