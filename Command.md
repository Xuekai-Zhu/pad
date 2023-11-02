### Model
- pre-trained
    - CodeT5-small: pre_trained_model/Salesforce/codet5-small
    - CodeT5-base: pre_trained_model/Salesforce/codet5-base
    - CodeT5-large: pre_trained_model/Salesforce/codet5-large
    - llama: /root/pubmodels/transformers/llama/llama-13b/llama-13b
    - chatglm: /root/pubmodels/transformers/chatglm-6b
- Trained Model
    - model/code-t5-small/code-t5-samll-enhanced-7time-learning-6e-5
    - model/code-t5-base/code-t5-base-enhanced-7time-learning-6e-5
    - model/code-t5-large/code-t5-large-enhanced-7time-learning-6e-5
- self-distillation
    - model/code-t5-small/model_for_distillation/code-t5-small-distillation-top-p-0.99
    - model/code-t5-base/self_distillation/code-t5-base-lr-6e-5-distillation
    - model/code-t5-large/self_distillation/code-t5-large-lr-6e-5-distillation

### Train Set
- GSM8K(orignal) dataset/grade-school-math/grade_school_math/train_rename.jsonl
- GSM8K dataset/gsm8k-generat-data/enhanced_data/7_time_data/train-enhanced.json
- GSM8K(filter data) dataset/gsm8k-generat-data/enhanced_data/filter_data
- coin_filp dataset/other_reasoning_datasets/symbolic_reasoning/coin_filp/train.json
- last_letter_concat dataset/other_reasoning_datasets/symbolic_reasoning/las_letter_concat/train.json
- strategy_qa  dataset/other_reasoning_datasets/commense_qa/strategy_qa/train.json


### Test Set
- GSM8K dataset/gsm8k-generat-data/gsm8k-1/test_file/test_add_code.json
- ASDiv dataset/ASDiv/data_refine.json
- SVAMP dataset/SVAMP/svamp_refine.json
- MA dataset/MultiArith/multi_arith_refine.json
- bbh dataset/BIG-Bench-Hard-main/bbh_processed/bbh.json
- strategy_qa dataset/other_reasoning_datasets/commense_qa/strategy_qa/test.json
- coin_flip dataset/other_reasoning_datasets/symbolic_reasoning/coin_filp/test.json
- last_letter_concatenation dataset/other_reasoning_datasets/symbolic_reasoning/las_letter_concat/test.json


### rebuutal data
- CoT rebuttal_clone_data/clone_CoT_data/train_add_cot_data_gpt-3.5.json
- pad text-davinci-002 rebuttal_clone_data/clone_pad_data_from_text-davinci-002/test/refine-train-davinci-002-delete-question.json \


