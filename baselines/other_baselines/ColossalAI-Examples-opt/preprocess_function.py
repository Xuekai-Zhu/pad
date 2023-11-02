from datasets import load_dataset, load_from_disk
from transformers import AutoTokenizer, OPTForCausalLM, default_data_collator
from colossalai.utils import get_current_device, get_dataloader
from torch.utils.data import DataLoader
import torch
    
def preprocess_function(example):
    padding = "max_length"
    max_input_length = 1024
    max_target_length = 128
    ignore_pad_token_for_loss = True
    tokenizer = AutoTokenizer.from_pretrained("facebook/opt-2.7b")

    
    # get instruction = definition + input
    inputs = [d + " " + i + " " + t for d, i, t in zip(example["definition"], example["inputs"], example["targets"])]
    # targets = [d + " "+ i for d, i in zip(inputs, example["targets"])]
    # targets = example["targets"]
    model_inputs = tokenizer(inputs, max_length=max_input_length, truncation=True, padding="max_length")
    model_inputs["labels"] = model_inputs["input_ids"].copy()
    # # Tokenize targets with the `text_target` keyword argument
    # labels = tokenizer(text_target=targets, max_length=max_target_length, padding=padding, truncation=True, padding="max_length")
    
    # If we are padding here, replace all tokenizer.pad_token_id in the labels by -100 when we want to ignore
    # padding in the loss.
    if padding == "max_length" and ignore_pad_token_for_loss == True:
            model_inputs["labels"] = [
                [(l if l != tokenizer.pad_token_id else -100) for l in label] for label in model_inputs["labels"]
            ]
    return model_inputs

def check_preprocess_data(data_path):
    tokenized_datasets = load_from_disk(data_path)
    print(tokenized_datasets)
    # exit(0)
    # split
    train_dataset = tokenized_datasets["train"]
    eval_dataset = tokenized_datasets["validation"]

    # data loader
    # train_dataloader = get_dataloader(train_dataset,
    #                                     shuffle=True,
    #                                     add_sampler=True,
    #                                     collate_fn=default_data_collator,
    #                                     batch_size=16)
    print(eval_dataset)
    eval_dataloader = DataLoader(eval_dataset,
                                collate_fn=default_data_collator,
                                batch_size=3,
                                drop_last=True
                                )
    for step, batch in enumerate(eval_dataloader):
        # batch = {k: v.cuda() for k, v in batch.items()}
        print("----------  {}   ------------".format(step))
        print(torch.sum(batch["labels"] == -100))
        print(batch["labels"].size())

if __name__ == '__main__':
    
    # config
    column_names = ["definition", "inputs", "targets"]
    # raw_datasets = load_dataset("Muennighoff/natural-instructions", split="validation")
    raw_datasets = load_dataset("Muennighoff/natural-instructions")
    
    # raw_datasets["train"].to_json("train.json")
    # raw_datasets["validation"].to_json("validation.json")
    # raw_datasets["test"].to_json("test.json")
    
    # tokenize_all_data
    tokenized_datasets = raw_datasets.map(
                    preprocess_function,
                    batched=True,
                    num_proc=8,
                    remove_columns=column_names,
                    # load_from_cache_file=not args.overwrite_cache,
                    desc="Running tokenizer on dataset",
                )
    # test
    # tokenized_datasets.to_json("test.json")
    
    tokenized_datasets["train"].to_json("tokenized_train.json")
    tokenized_datasets["validation"].to_json("tokenized_validation.json")
    tokenized_datasets["test"].to_json("tokenized_test.json")

    # eval_dataloader = DataLoader(tokenized_datasets,
    #                             collate_fn=default_data_collator,
    #                             batch_size=3,
    #                             # drop_last=True
    #                             )
    # print(eval_dataloader)
    # for step, batch in enumerate(eval_dataloader):
    #     # batch = {k: v.cuda() for k, v in batch.items()}
    #     print("----------  {}   ------------".format(step))
    #     print(torch.sum(batch["labels"] == -100))
    #     print(batch["labels"].size())
    # # save
    # tokenized_datasets.save_to_disk("baselines/ColossalAI-Examples-opt/preprocess_data")
    # # load local file
    # tokenized_datasets = load_from_disk("baselines/ColossalAI-Examples-opt/tokenize_natural_instruction_data")

    # check
    # check_preprocess_data("../../dataset/tokenize_natural_instruction_v2_data")

    