#!/usr/bin/env python
# coding=utf-8
# Copyright 2021 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Fine-tuning the library models for causal language modeling (GPT, GPT-2, CTRL, ...)
on a text file or a dataset without using HuggingFace Trainer.

Here is the full list of checkpoints on the hub that can be fine-tuned by this script:
https://huggingface.co/models?filter=text-generation
"""
# You can also adapt this script on your own causal language modeling task. Pointers for this are left as comments.

import math
import os
import random
from itertools import chain
import time
from functools import partial

import datasets
import torch
import torch.distributed as dist
from datasets import load_dataset, load_from_disk
from torch.utils.data import DataLoader
from colossalai.core import global_context as gpc
from colossalai.context import ParallelMode
from tqdm.auto import tqdm
import colossalai
from colossalai.logging import get_dist_logger, disable_existing_loggers
from titans.utils import barrier_context

import transformers

from transformers import CONFIG_MAPPING, MODEL_MAPPING, AutoConfig, OPTForCausalLM, AutoTokenizer, SchedulerType, GPT2Tokenizer, default_data_collator, get_scheduler
                          
from transformers.utils.versions import require_version

import colossalai
from colossalai.logging import disable_existing_loggers, get_dist_logger
from colossalai.nn.optimizer.gemini_optimizer import GeminiAdamOptimizer
from colossalai.nn.parallel import GeminiDDP
from colossalai.utils import get_current_device, get_dataloader
from colossalai.utils.model.colo_init_context import ColoInitContext
from data_preprocess import NI_DataFunction

# def get_data(batch_size, seq_len, vocab_size):
#     input_ids = torch.randint(0, vocab_size, (batch_size, seq_len), device=torch.cuda.current_device())
#     attention_mask = torch.ones_like(input_ids)
#     return input_ids, attention_mask


require_version("datasets>=1.8.0", "To fix: pip install -r examples/pytorch/language-modeling/requirements.txt")

MODEL_CONFIG_CLASSES = list(MODEL_MAPPING.keys())
MODEL_TYPES = tuple(conf.model_type for conf in MODEL_CONFIG_CLASSES)


def get_time_stamp():
    torch.cuda.synchronize()
    return time.time()


def get_tflops(model_numel, batch_size, seq_len, step_time):
    return model_numel * batch_size * seq_len * 8 / 1e12 / (step_time + 1e-12)


def parse_args():
    parser = colossalai.get_default_parser()
    parser.add_argument(
        "--dataset_name",
        type=str,
        default=None,
        help="The name of the dataset to use (via the datasets library).",
    )
    parser.add_argument(
        "--dataset_config_name",
        type=str,
        default=None,
        help="The configuration name of the dataset to use (via the datasets library).",
    )
    parser.add_argument("--train_file",
                        type=str,
                        default=None,
                        help="A csv or a json file containing the training data.")
    parser.add_argument("--validation_file",
                        type=str,
                        default=None,
                        help="A csv or a json file containing the validation data.")
    parser.add_argument(
        "--validation_split_percentage",
        default=5,
        help="The percentage of the train set used as validation set in case there's no validation split",
    )
    parser.add_argument(
        "--local_train_dataset_path",
        type=str,
        default=None,
        help="The path of the local train dataset to use.",
    )
    parser.add_argument(
        "--local_validation_dataset_path",
        type=str,
        default=None,
        help="The path of the local validation dataset to use.",
    )
    parser.add_argument(
        "--model_name_or_path",
        type=str,
        help="Path to pretrained model or model identifier from huggingface.co/models.",
        required=True,
    )
    parser.add_argument(
        "--config_name",
        type=str,
        default=None,
        help="Pretrained config name or path if not the same as model_name",
    )
    parser.add_argument(
        "--batch_size",
        type=int,
        default=8,
        help="Batch size (per dp group) for the training dataloader.",
    )
    parser.add_argument(
        "--tokenizer_name",
        type=str,
        default=None,
        help="Pretrained tokenizer name or path if not the same as model_name",
    )
    parser.add_argument(
        "--per_device_eval_batch_size",
        type=int,
        default=8,
        help="Batch size (per device) for the evaluation dataloader.",
    )
    parser.add_argument(
        "--learning_rate",
        type=float,
        default=5e-5,
        help="Initial learning rate (after the potential warmup period) to use.",
    )
    parser.add_argument("--weight_decay", type=float, default=0.0, help="Weight decay to use.")
    parser.add_argument("--num_train_epochs", type=int, default=2, help="Total number of training epochs to perform.")
    parser.add_argument(
        "--max_train_steps",
        type=int,
        default=None,
        help="Total number of training steps to perform.",
    )
    parser.add_argument(
        "--gradient_accumulation_steps",
        type=int,
        default=1,
        help="Number of updates steps to accumulate before performing a backward/update pass.",
    )
    parser.add_argument(
        "--lr_scheduler_type",
        type=SchedulerType,
        default="linear",
        help="The scheduler type to use.",
        choices=["linear", "cosine", "cosine_with_restarts", "polynomial", "constant", "constant_with_warmup"],
    )
    parser.add_argument("--num_warmup_steps",
                        type=int,
                        default=0,
                        help="Number of steps for the warmup in the lr scheduler.")
    parser.add_argument("--output_dir", type=str, default=None, help="Where to store the final model.")
    parser.add_argument("--seed", type=int, default=None, help="A seed for reproducible training.")
    parser.add_argument(
        "--model_type",
        type=str,
        default=None,
        help="Model type to use if training from scratch.",
        choices=MODEL_TYPES,
    )
    parser.add_argument(
        "--max_source_length",
        type=int,
        default=1024,
        help=(
            "The maximum total input sequence length after "
            "tokenization.Sequences longer than this will be truncated, sequences shorter will be padded."
        ),
    )
    parser.add_argument(
        "--max_target_length",
        type=int,
        default=128,
        help=(
            "The maximum total sequence length for target text after "
            "tokenization. Sequences longer than this will be truncated, sequences shorter will be padded."
            "during ``evaluate`` and ``predict``."
        ),
    )
    parser.add_argument(
        "--ignore_pad_token_for_loss",
        type=bool,
        default=True,
        help="Whether to ignore the tokens corresponding to padded labels in the loss computation or not.",
    )
    parser.add_argument(
        "--preprocessing_num_workers",
        type=int,
        default=None,
        help="The number of processes to use for the preprocessing.",
    )
    parser.add_argument("--overwrite_cache",
                        type=bool,
                        default=False,
                        help="Overwrite the cached training and evaluation sets")
    parser.add_argument("--no_keep_linebreaks",
                        action="store_true",
                        help="Do not keep line breaks when using TXT files.")
    
    parser.add_argument(
        "--checkpointing_steps",
        type=str,
        default=None,
        help="Whether the various states should be saved at the end of every n steps, or 'epoch' for each epoch.",
    )
    parser.add_argument(
        "--resume_from_checkpoint",
        type=str,
        default=None,
        help="If the training should continue from a checkpoint folder.",
    )
    parser.add_argument(
        "--with_tracking",
        action="store_true",
        help="Whether to enable experiment trackers for logging.",
    )
    parser.add_argument(
        "--report_to",
        type=str,
        default="all",
        help=('The integration to report the results and logs to. Supported platforms are `"tensorboard"`,'
              ' `"wandb"` and `"comet_ml"`. Use `"all"` (default) to report to all integrations.'
              "Only applicable when `--with_tracking` is passed."),
    )

    parser.add_argument("--mem_cap", type=int, default=0, help="use mem cap")
    parser.add_argument("--init_in_cpu", action='store_true', default=False, help="init training model in cpu")
    args = parser.parse_args()

    # Sanity checks
    if args.dataset_name is None and args.local_train_dataset_path is None and args.local_validation_dataset_path is None:
        raise ValueError("Need either a dataset name or a training/validation file.")
    else:
        if args.train_file is not None:
            extension = args.train_file.split(".")[-1]
            assert extension in ["csv", "json", "txt"], "`train_file` should be a csv, json or txt file."
        if args.validation_file is not None:
            extension = args.validation_file.split(".")[-1]
            assert extension in ["csv", "json", "txt"], "`validation_file` should be a csv, json or txt file."

    return args


def colo_memory_cap(size_in_GB):
    from colossalai.utils import colo_device_memory_capacity, colo_set_process_memory_fraction, get_current_device
    cuda_capacity = colo_device_memory_capacity(get_current_device())
    if size_in_GB * (1024**3) < cuda_capacity:
        colo_set_process_memory_fraction(size_in_GB * (1024**3) / cuda_capacity)
        print("Using {} GB of GPU memory".format(size_in_GB))


def main():
    args = parse_args()
    disable_existing_loggers()
    colossalai.launch_from_torch({})
    logger = get_dist_logger()
    is_main_process = dist.get_rank() == 0

    if is_main_process:
        datasets.utils.logging.set_verbosity_warning()
        transformers.utils.logging.set_verbosity_info()
    else:
        datasets.utils.logging.set_verbosity_error()
        transformers.utils.logging.set_verbosity_error()

    if args.mem_cap > 0:
        colo_memory_cap(args.mem_cap)

    # If passed along, set the training seed now.
    if args.seed is not None:
        torch.mannul_seed(args.seed)
        logger.info(f"Rank {dist.get_rank()}: random seed is set to {args.seed}")
    # Handle the repository creation
    with barrier_context():
        if args.output_dir is not None:
            os.makedirs(args.output_dir, exist_ok=True)
    
    # See more about loading any type of standard or custom dataset (from files, python dict, pandas DataFrame, etc) at
    # https://huggingface.co/docs/datasets/loading_datasets.html.

    # Load pretrained model and tokenizer
    #
    # In distributed training, the .from_pretrained methods guarantee that only one local process can concurrently
    # download model & vocab.
    if args.config_name:
        config = AutoConfig.from_pretrained(args.config_name)
    elif args.model_name_or_path:
        config = AutoConfig.from_pretrained(args.model_name_or_path)
    else:
        config = CONFIG_MAPPING[args.model_type]()
        logger.warning("You are instantiating a new config instance from scratch.")
    logger.info("Model config has been created", ranks=[0])

    if args.model_name_or_path == 'facebook/opt-13b':
        tokenizer = GPT2Tokenizer.from_pretrained(args.model_name_or_path)
    else:
        tokenizer = AutoTokenizer.from_pretrained(args.model_name_or_path)
    logger.info(f"{tokenizer.__class__.__name__} has been created", ranks=[0])

    if args.init_in_cpu:
        init_dev = torch.device('cpu')
    else:
        init_dev = get_current_device()

    # build model
    # if args.model_name_or_path is None:
    if args.model_name_or_path is None or args.model_name_or_path == 'facebook/opt-13b':
        # currently, there has a bug in pretrained opt-13b
        # we can not import it until huggingface fix it
        logger.info("Train a new model from scratch", ranks=[0])
        with ColoInitContext(device=init_dev, dtype=torch.half):
            model = OPTForCausalLM(config)
    else:
        logger.info("Finetune a pre-trained model", ranks=[0])
        with ColoInitContext(device=init_dev, dtype=torch.half):
            model = OPTForCausalLM.from_pretrained(args.model_name_or_path,
                                                   from_tf=bool(".ckpt" in args.model_name_or_path),
                                                   config=config,
                                                   local_files_only=False)

    # enable graident checkpointing
    model.gradient_checkpointing_enable()

    numel = sum([p.numel() for p in model.parameters()])
    PLACEMENT_POLICY = "cpu"
    model = GeminiDDP(model, device=get_current_device(), placement_policy=PLACEMENT_POLICY, pin_memory=True)
    logger.info(f'{model.__class__.__name__} has been created', ranks=[0])

    
    
  
    # Load prepocess data from disk
    # pre_tokenized_datasets = NI_DataFunction(args.local_dataset_train_path)
    train_dataset = NI_DataFunction(args.local_train_dataset_path)
    eval_dataset = NI_DataFunction(args.local_validation_dataset_path)
    
    logger.info("Dataset is prepared", ranks=[0])
    
    # Log a few random samples from the training set:
    # for index in random.sample(range(len(train_dataset)), 3):
    #     logger.info(f"Sample {index} of the training set: {train_dataset[index]}.")

    # DataLoaders creation:
    train_dataloader = get_dataloader(train_dataset,
                                      shuffle=True,
                                      add_sampler=True,
                                      collate_fn=default_data_collator,
                                      batch_size=args.batch_size)
    eval_dataloader = DataLoader(eval_dataset,
                                 collate_fn=default_data_collator,
                                 batch_size=args.per_device_eval_batch_size)
    logger.info("Dataloaders have been created", ranks=[0])

   # Optimizer
    optimizer = GeminiAdamOptimizer(model, lr=args.learning_rate, initial_scale=2**5, gpu_margin_mem_ratio=0.0)

   # Scheduler and math around the number of training steps.
    overrode_max_train_steps = False
    num_update_steps_per_epoch = math.ceil(len(train_dataloader) / args.gradient_accumulation_steps)
    if args.max_train_steps is None:
        args.max_train_steps = args.num_train_epochs * num_update_steps_per_epoch
        overrode_max_train_steps = True
    lr_scheduler = get_scheduler(
        name=args.lr_scheduler_type,
        optimizer=optimizer,
        num_warmup_steps=args.num_warmup_steps,
        num_training_steps=args.max_train_steps,
    )

    # We need to recalculate our total training steps as the size of the training dataloader may have changed.
    num_update_steps_per_epoch = math.ceil(len(train_dataloader) / args.gradient_accumulation_steps)
    if overrode_max_train_steps:
        args.max_train_steps = args.num_train_epochs * num_update_steps_per_epoch
    # Afterwards we recalculate our number of training epochs
    args.num_train_epochs = math.ceil(args.max_train_steps / num_update_steps_per_epoch)

    # Train!
    total_batch_size = args.batch_size * gpc.get_world_size(ParallelMode.DATA)

    logger.info("***** Running training *****", ranks=[0])
    logger.info(f"  Num examples = {len(train_dataset)}", ranks=[0])
    logger.info(f"  Num Epochs = {args.num_train_epochs}", ranks=[0])
    logger.info(f"  Instantaneous batch size per device = {args.batch_size}", ranks=[0])
    logger.info(f"  Total train batch size (w. parallel, distributed & accumulation) = {total_batch_size}", ranks=[0])
    logger.info(f"  Gradient Accumulation steps = {args.gradient_accumulation_steps}", ranks=[0])
    logger.info(f"  Total optimization steps = {args.max_train_steps}", ranks=[0])

    # Only show the progress bar once on each machine.
    progress_bar = tqdm(range(args.max_train_steps), disable=not is_main_process)
    completed_steps = 0
    starting_epoch = 0
    global_step = 0

    for epoch in range(starting_epoch, args.num_train_epochs):

        if completed_steps >= args.max_train_steps:
            break

        model.train()
        for step, batch in enumerate(train_dataloader):
            batch = {k: v.cuda() for k, v in batch.items()}
            
            outputs = model(**batch, use_cache=False)
            st_time = time.time()
            loss = outputs['loss']
            optimizer.backward(loss)

            if step % args.gradient_accumulation_steps == 0 or step == len(train_dataloader) - 1:
                optimizer.step()
                lr_scheduler.step()
                optimizer.zero_grad()
                progress_bar.update(1)
                completed_steps += 1
            
            torch.cuda.synchronize()
            step_time = time.time() - st_time
            global_step += 1
            logger.info("Global step {} finished; Time {}; Loss {}".format(global_step + 1, step_time, loss), ranks=[0])

        if completed_steps >= args.max_train_steps:
            break

        model.eval()
        losses = []
        for step, batch in enumerate(eval_dataloader):
            with torch.no_grad():
                batch = {k: v.cuda() for k, v in batch.items()}
                outputs = model(**batch)

        loss = outputs['loss'].unsqueeze(0)
        losses.append(loss)

        losses = torch.cat(losses)
        losses = losses[:len(eval_dataset)]
        try:
            eval_loss = torch.mean(losses)
            perplexity = math.exp(eval_loss)
        except OverflowError:
            perplexity = float("inf")

        logger.info(f"Epoch {epoch}: perplexity: {perplexity} eval_loss: {eval_loss}", ranks=[0])

    if args.output_dir is not None:
        model_state = model.state_dict()
        if is_main_process:
            torch.save(model_state, args.output_dir + '/epoch_{}_model.pth'.format(completed_steps))
        dist.barrier()
        # load_state = torch.load(args.output_dir + '/epoch_{}_model.pth'.format(completed_steps))
        # model.load_state_dict(load_state, strict=False)

    logger.info("Training finished", ranks=[0])


if __name__ == "__main__":
    main()