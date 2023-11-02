python run_clm_no_trainer.py \
    --train_file dataset/PAL_data/all.json \
    --model_name_or_path pre_trained_model/facebook/opt-350m \
    --output_dir model/opt-iml-code-generate-tuning \
    --per_device_train_batch_size 8 \
    --per_device_eval_batch_size 8 \
    --num_train_epochs 100