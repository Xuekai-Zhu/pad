python run_clm_no_trainer-t5.py \
    --train_file dataset/PAL_data/all.json \
    --model_name_or_path pre_trained_model/flan-t5-large \
    --output_dir model/t5-code-generate-tuning \
    --per_device_train_batch_size 8 \
    --per_device_eval_batch_size 8 \
    --num_train_epoch 30