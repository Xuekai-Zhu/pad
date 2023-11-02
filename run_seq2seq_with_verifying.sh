CUDA_VISIBLE_DEVICES=4 python run_seq2seq.py \
    --model_name_or_path model/code-t5-large/self_distillation/code-t5-large-lr-6e-5-distillation \
    --do_predict \
    --num_beams=10 \
    --chain_beams=10 \
    --test_file dataset/gsm8k-generat-data/gsm8k-1/test_file/test_add_code.json \
    --output_dir baselines/chain_size/size_10/code-t5-large \
    --per_device_eval_batch_size=4 \
    --predict_with_generate