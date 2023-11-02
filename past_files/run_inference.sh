deepspeed --num_nodes 1 --num_gpus 1 inference-test.py \
    --name model/code-t5 \
    --batch_size 32 \
    --local_dataset_path dataset/gsm8k-0306/test_file/refine-test_add_code.json \
    --output_dir model/code-t5 \
    # --greedy 
    # --add_solution 