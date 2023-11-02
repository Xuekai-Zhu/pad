---
license: apache-2.0
tags:
- codet5
datasets:
- code_search_net
inference: false
---

# CodeT5 (base-sized model) 

Pre-trained CodeT5 model. It was introduced in the paper [CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models
for Code Understanding and Generation](https://arxiv.org/abs/2109.00859) by Yue Wang, Weishi Wang, Shafiq Joty, Steven C.H. Hoi and first released in [this repository](https://github.com/salesforce/CodeT5). 

Disclaimer: The team releasing CodeT5 did not write a model card for this model so this model card has been written by the Hugging Face team (more specifically, [nielsr](https://huggingface.co/nielsr)).

## Model description

From the abstract:

"We present CodeT5, a unified pre-trained encoder-decoder Transformer model that better leverages the code semantics conveyed from the developer-assigned identifiers. Our model employs a unified framework to seamlessly support both code understanding and generation tasks and allows for multi-task learning. Besides, we propose a novel identifier-aware pre-training task that enables the model to distinguish which code tokens are identifiers and to recover them when they are masked. Furthermore, we propose to exploit the user-written code comments with a bimodal dual generation task for better NL-PL alignment. Comprehensive experiments show that CodeT5 significantly outperforms prior methods on understanding tasks such as code defect detection and clone detection, and generation tasks across various directions including PL-NL, NL-PL, and PL-PL. Further analysis reveals that our model can better capture semantic information from code."

## Intended uses & limitations

This repository contains the pre-trained model only, so you can use this model for (among other tasks) masked span prediction, as shown in the code example below. However, the main use of this model is to fine-tune it for a downstream task of interest, such as:
* code summarization
* code generation
* code translation
* code refinement
* code defect detection
* code clone detection. 

Supervised datasets for code can be found [here](https://huggingface.co/datasets?languages=languages:code).
See the [model hub](https://huggingface.co/models?search=salesforce/codet) to look for fine-tuned versions on a task that interests you.

### How to use

Here is how to use this model:

```python
from transformers import RobertaTokenizer, T5ForConditionalGeneration

tokenizer = RobertaTokenizer.from_pretrained('Salesforce/codet5-base')
model = T5ForConditionalGeneration.from_pretrained('Salesforce/codet5-base')

text = "def greet(user): print(f'hello <extra_id_0>!')"
input_ids = tokenizer(text, return_tensors="pt").input_ids

# simply generate a single sequence
generated_ids = model.generate(input_ids, max_length=8)
print(tokenizer.decode(generated_ids[0], skip_special_tokens=True))
# this prints "{user.username}"
```

## Training data

The CodeT5 model was pretrained on CodeSearchNet [Husain et al., 2019](https://arxiv.org/abs/1909.09436). Additionally, the authors collected two datasets of C/CSharp from [BigQuery1](https://console.cloud.google.com/marketplace/details/github/github-repos) to ensure that all downstream tasks have overlapped programming languages with the pre-training data. In total, around 8.35 million instances are used for pretraining. 

## Training procedure

### Preprocessing

This model uses a code-specific BPE (Byte-Pair Encoding) tokenizer trained using the [HuggingFace Tokenizers](https://github.com/huggingface/tokenizers) library. One can prepare text (or code) for the model using RobertaTokenizer, with the files from this repository.

## Evaluation results

For evaluation results on several downstream benchmarks, we refer to the paper.

### BibTeX entry and citation info

```bibtex
@misc{wang2021codet5,
      title={CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models for Code Understanding and Generation}, 
      author={Yue Wang and Weishi Wang and Shafiq Joty and Steven C. H. Hoi},
      year={2021},
      eprint={2109.00859},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```