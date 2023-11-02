# CUDA_VISIBLE_DEVICES=1 
python run_seq2seq.py \
    --model_name_or_path model/code-t5-small/code-t5-samll-enhanced-7time-learning-6e-5 \
    --teacher_model_name_or_path model/code-t5-small/code-t5-samll-enhanced-7time-learning-6e-5 \
    --do_train \
    --do_eval \
    --learning_rate=6e-5 \
    --train_file dataset/gsm8k-generat-data/enhanced_data/7_time_data/train-enhanced.json \
    --output_dir model/code-t5-small/model_for_distillation/code-t5-small-distillation-top-p-0.99 \
    --per_device_train_batch_size=32 \
    --per_device_eval_batch_size=32 \
    --evaluation_strategy "epoch" \
    --save_strategy "epoch" \
    --num_train_epochs 50 \
    --overwrite_output_dir \
    --load_best_model_at_end=True \
    --report_to wandb
