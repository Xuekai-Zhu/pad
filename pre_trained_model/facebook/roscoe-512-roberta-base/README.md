---
license: cc-by-nc-4.0
---
# roscoe-512-roberta-base

## Model description
Sentence embedding model for reasoning steps.

To obtain reasoning step embeddings, we finetune SimCSE (Gao et al., 2021), a
supervised sentence similarity model extending the RoBERTa word embedding model (Liu et al., 2019) on
multi-step reasoning datasets we listed in §5 (see details in Golovneva et al., 2022). SimCSE is a contrastive learning model
that is trained on triplets of reference reasoning steps, positive and hard-negative hypothesis reasoning steps
to minimize the cross-entropy objective with in-batch negatives. For contrastive learning, we use the context
and reference reasoning steps as a positive sample, and context and perturbed reference steps as
hard-negative pairs. With finetuned model we embed each individual step, as well as a reasoning chain as a
whole. We use the pretrained checkpoint of supervised SimCSE model sup-simcse-roberta-base to initialize
our model, and further train it for five epochs on our synthetic train data.

## Training data
To train the model, we construct dataset by generating perturbations — i.e.,
deterministic modifications — on half of the reference reasoning steps in the following sets: Entailment-Bank
(deductive reasoning), ProofWriter (logical reasoning); three arithmetic reasoning datasets MATH, ASDIV and AQUA; EQASC 
(explanations for commonsense question answering), and StrategyQA (question answering with implicit reasoning strategies).

## References

1. Tianyu Gao, Xingcheng Yao, and Danqi Chen. Simcse: Simple contrastive learning of sentence embeddings.
arXiv preprint arXiv:2104.08821, 2021.
2. Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Luke Zettlemoyer, and Veselin Stoyanov. Roberta: A robustly optimized bert pretraining approach. arXiv
preprint arXiv:1907.11692, 2019.
3. Olga Golovneva, Moya Chen, Spencer Poff, Martin Corredor, Luke Zettlemoyer, Maryam Fazel-Zarandi, and Asli Celikyilmaz. 
ROSCOE: A Suite of Metrics for Scoring Step-by-Step Reasoning. arXiv:2212.07919, 2022.
 
## Citation
@article{golovneva2022roscoe,
  title={{ROSCOE}: A Suite of Metrics for Scoring Step-by-Step Reasoning},
  author={Golovneva, Olga and Chen, Moya and Poff, Spencer and Corredor, Martin and Zettlemoyer, Luke and Fazel-Zarandi, Maryam and Celikyilmaz, Asli},
  journal={arXiv preprint arXiv:2212.07919},
  year={2022}
}