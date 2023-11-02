set -x
export BS=16
export MODEL=2.7b
export GPUNUM=1
export OUTPUT=./model
export TRAINFILE=dataset/natural-instruction-v2-json/tokenized_text/tokenized_train.json
export VALFILE=dataset/natural-instruction-v2-json/tokenized_text/tokenized_validation.json


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
  train_gemini_opt_0203.py \
  --local_train_dataset_path ${TRAINFILE} \
  --local_validation_dataset_path ${VALFILE} \
  --mem_cap ${MEMCAP} \
  --learning_rate 1e-5 \
  --output_dir ${OUTPUT} \
  --model_name_or_path ${MODLE_PATH} \
  --batch_size ${BS} 2>&1 | tee ./logs/${MODEL}_bs_${BS}_cap_${MEMCAP}_gpu_${GPUNUM}.log