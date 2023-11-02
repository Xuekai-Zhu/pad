from datasets import load_dataset


# Get the datasets: you can either provide your own CSV/JSON/TXT training and evaluation files (see below)
    # or just provide the name of one of the public datasets available on the hub at https://huggingface.co/datasets/
    # (the dataset will be downloaded automatically from the datasets Hub).
    #
    # For CSV/JSON files, this script will use the column called 'text' or the first column if no column called
    # 'text' is found. You can easily tweak this behavior (see below).
    #
    # In distributed training, the load_dataset function guarantee that only one local process can concurrently
    # download the dataset.
    # logger.info("Start preparing dataset", ranks=[0])
    # if args.dataset_name is not None:
    #     # Downloading and loading a dataset from the hub.
    #     raw_datasets = load_dataset(args.dataset_name, args.dataset_config_name)
    #     # If no validation data is there, validation_split_percentage will be used to divide the dataset.
    #     if "validation" not in raw_datasets.keys():
    #         raw_datasets["validation"] = load_dataset(
    #             args.dataset_name,
    #             args.dataset_config_name,
    #             split=f"train[:{args.validation_split_percentage}%]",
    #         )
    #         raw_datasets["train"] = load_dataset(
    #             args.dataset_name,
    #             args.dataset_config_name,
    #             split=f"train[{args.validation_split_percentage}%:]",
    #         )
    # else:
    #     data_files = {}
    #     dataset_args = {}
    #     if args.train_file is not None:
    #         data_files["train"] = args.train_file
    #     if args.validation_file is not None:
    #         data_files["validation"] = args.validation_file
    #     extension = args.train_file.split(".")[-1]
    #     if extension == "txt":
    #         extension = "text"
    #         dataset_args["keep_linebreaks"] = not args.no_keep_linebreaks
    #     raw_datasets = load_dataset(extension, data_files=data_files, **dataset_args)
    #     # If no validation data is there, validation_split_percentage will be used to divide the dataset.
    #     if "validation" not in raw_datasets.keys():
    #         raw_datasets["validation"] = load_dataset(
    #             extension,
    #             data_files=data_files,
    #             split=f"train[:{args.validation_split_percentage}%]",
    #             **dataset_args,
    #         )
    #         raw_datasets["train"] = load_dataset(
    #             extension,
    #             data_files=data_files,
    #             split=f"train[{args.validation_split_percentage}%:]",
    #             **dataset_args,
    #         )
    # logger.info("Dataset is prepared", ranks=[0])