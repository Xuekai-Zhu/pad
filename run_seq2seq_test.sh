CUDA_VISIBLE_DEVICES=0 python run_seq2seq.py \
    --model_name_or_path model/one-time-data/codet5-small \
    --do_predict \
    --test_file dataset/MultiArith/multi_arith_refine.json \
    --output_dir model/one-time-data/codet5-small/MultiArith \
    --per_device_eval_batch_size=8 \
    --predict_with_generate