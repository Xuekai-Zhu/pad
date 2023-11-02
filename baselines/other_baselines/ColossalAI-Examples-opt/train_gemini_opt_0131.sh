set -x
export BS=16
# export MEMCAP=0
export MODEL=2.7b
export GPUNUM=2
export OUTPUT=./model
# export BLOCKSIZE=1024


# export BS=${BS:-16}
export MEMCAP=${MEMCAP:-0}
# Acceptable values include `125m`, `350m`, `1.3b`, `2.7b`, `6.7`, `13b`, `30b`, `66b`. For `175b`
# export MODEL=${MODEL:-"125m"}
# export GPUNUM=${GPUNUM:-1}

# make directory for logs
mkdir -p ./logs

export MODLE_PATH="facebook/opt-${MODEL}"

# HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1
torchrun \
  --nproc_per_node ${GPUNUM} \
  --master_port 19198 \
  train_gemini_opt_0131.py \
  --dataset_name wikitext \
  --dataset_config_name wikitext-2-raw-v1 \
  --mem_cap ${MEMCAP} \
  --output_dir ${OUTPUT} \
  --model_name_or_path ${MODLE_PATH} \
  # --block_size ${BLOCKSIZE} \
  --batch_size ${BS} 2>&1 | tee ./logs/colo_${MODEL}_bs_${BS}_cap_${MEMCAP}_gpu_${GPUNUM}.log