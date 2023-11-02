---
tags:
- generated_from_trainer
model-index:
- name: code-t5-base
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# code-t5-base

This model is a fine-tuned version of [model/code-t5-base/self_distillation/code-t5-base-lr-6e-5-distillation](https://huggingface.co/model/code-t5-base/self_distillation/code-t5-base-lr-6e-5-distillation) on an unknown dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Framework versions

- Transformers 4.27.0
- Pytorch 1.12.1
- Datasets 2.2.1
- Tokenizers 0.13.3
