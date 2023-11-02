import torch
from typing import Any, Dict, Iterable, List, Optional, Tuple, Union
import json
import re
from nltk import sent_tokenize
from tqdm import tqdm
import numpy as np
from sentence_transformers import SentenceTransformer
from simcse import SimCSE
import pathlib
import os
from collections import defaultdict


SIM_SCE_MODELS_DICT = {
    "princeton-nlp/sup-simcse-roberta-large": "roberta-large",
    "princeton-nlp/sup-simcse-roberta-base": "roberta-base",
    "princeton-nlp/sup-simcse-bert-base-uncased": "bert-base-uncased",
    "facebook/roscoe-512-roberta-base": "roberta-base",
}

SENT_TRANS = "sentence_transformer"
SIMSCE = "sim_sce"
FAITHFUL_SENT = "faithfulness"
# sentence to word embedding models
TRANSFORMER_MODELS_DICT = {
    "all-mpnet-base-v2": "microsoft/mpnet-base",
    "all-MiniLM-L6-v2": "nreimers/MiniLM-L6-H384-uncased",
}
SIM_SCE_MODELS_DICT = {
    "princeton-nlp/sup-simcse-roberta-large": "roberta-large",
    "princeton-nlp/sup-simcse-roberta-base": "roberta-base",
    "princeton-nlp/sup-simcse-bert-base-uncased": "bert-base-uncased",
    "facebook/roscoe-512-roberta-base": "roberta-base",
}
class Chain:
    def __init__(self, line: List[str]) -> None:
        self.chain = self.parse_chain(line)
        self.sentence_embeddings = None
        self.whole_chain_embedding = None

    def parse_chain(self, chain: List[str]) -> List[str]:
        """
        Change formatting Returns list of steps in reasoning chain.
        """
        return chain

    def set_sentence_embeddings(self, embeddings: List[List[float]]):
        self.sentence_embeddings = embeddings

    def set_whole_chain_embedding(self, embeddings: List[float]):
        self.whole_chain_embedding = embeddings


class ReasoningSteps(Chain):
    def __init__(self, line: str, type="regular") -> None:
        self.chain = self.parse_chain(line, type=type)

    def parse_chain(self, chain: str, type: str) -> List[str]:
        """
        Change formatting.

        Returns list of steps in reasoning chain.
        """
        if type == "regular":
            return sent_tokenize(chain)
        elif type == "code":
            return re.split('\n\n|\n', chain)

def batch_parse_chain(chains, type=None):
        """
        Change formatting.

        Returns list of steps in reasoning chain.
        """
        chain_list = []
        # before_list = []
        # for i, j in zip(chains,:
        if type == "regular":
            # chain_list.append(sent_tokenize(chains)) 
            all_chain = sent_tokenize(chains)
            
        elif type == "code":
            
            # all_chain = re.split('\n\n|\n', chains)
            all_chain = all_chain = re.findall('(.*?(?:\n\n|\n))', chains, re.DOTALL)
            all_chain = [chain.strip() for chain in all_chain if chain.strip()]

            # if j >= len(all_chain):
            #     j = -1
            # step = all_chain[j]
            
            # chain_list.append(all_chain)
            
            # step_index = i.find(step)
            # extracted = i[:step_index + len(step)]
            # before_list.append(extracted)
                
        # if return_before_step:
            
        #     return chain_list, before_list
        
        # else:
        return all_chain


def cosine_similarity_scaled(list1: np.ndarray, list2: np.ndarray) -> float:
    """
    Normalized cosine similarity for *normalized* embeddings.

    Normalized cosine similarity takes values from [0;1]
    """
    cosine_sim = np.dot(list1, list2) / (np.linalg.norm(list1) * np.linalg.norm(list2))
    return (1.0 + cosine_sim) / 2.0


def embedding_alignment(ref_emb: np.ndarray, hypo_emb: np.ndarray) -> List[float]:
    """
    Return embedding matching alignment for each item in hypo_emb
    ref_emb: list of reference embeddings
    hypo_emb: list oh hypothesises embeddings
    """
    scores = []
    for he in hypo_emb:
        # some embeddings can be empty. For example, for latex-style equations, or empty string
        if len(he) > 0:
            out = [cosine_similarity_scaled(he, re) for re in ref_emb if len(re) > 0]
            if len(out) > 0:
                scores.append(max(out))
    return scores


def al_mean(alignment_scores) -> float:
    if len(alignment_scores) == 0:
        return 0.0
    return sum(alignment_scores) / len(alignment_scores)

class ReasoningEvaluator():
    def __init__(
        self,
        model_type: str,
        transformer_model: str,
        # discourse_batch: int,
        # coherence_batch: int,
        hypos=[],
        context=[],
        # hypos: List[Chain],
        # context: List[Chain],
        score_types=None,
        ):
        self.device = (
            torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
        )
        # self.references = references
        self.hypos = hypos
        self.context = context
        self.sentence_model, self.word_model_name = self._create_model(
                model_type, transformer_model
            )
    
    def _create_model(
        self, type: str, sentence_embedding_model: str
    ) -> Tuple[SentenceTransformer, str]:
        if type == SIMSCE and sentence_embedding_model in SIM_SCE_MODELS_DICT.keys():
            # should be auto-uploaded to CUDA if GPU is available
            return (
                SimCSE(sentence_embedding_model),
                SIM_SCE_MODELS_DICT[sentence_embedding_model],
            )
        elif (
            type == SENT_TRANS
            and sentence_embedding_model in TRANSFORMER_MODELS_DICT.keys()
        ):
            # Load model from HuggingFace Hub
            model = SentenceTransformer(sentence_embedding_model)
            model.eval().to(self.device)
            return (
                model,
                TRANSFORMER_MODELS_DICT[sentence_embedding_model],
            )

    def set_hypos(self, hypos) -> None:
        self.hypos = hypos

    # def set_references(self, references: List[Chain]) -> None:
    #     self.references = references

    def set_context(self, context) -> None:
        self.context = context
    
    def update_evaluator(self, context=None, reasoning_code=None):
        hypothesises = []
        contexts = []
        # refs = []
        # with open(in_file) as _f:
        #     for line in _f:
        #         jline = json.loads(line)
        for i, j in zip(context, reasoning_code):
            h_chain = ReasoningSteps(j, type="code")

            context = ReasoningSteps(i)

            hypothesises.append(h_chain)
            contexts.append(context)

        self.set_hypos(hypothesises)
        self.set_context(contexts)
        # self.set_references(refs)
    
    def embed_sentences(self, reasoning: List[str]) -> List[List[float]]:
        """Input:
            reasoning: list of strings (reasoning steps, for ex)
        Returns a list of embeddings, one per sentence
        """
        if len(reasoning) == 0:
            return [[]]
        embeddings = []
        with torch.no_grad():
            embeddings = self.sentence_model.encode(reasoning)
        # normalize
        if torch.is_tensor(embeddings[0]):
            embeddings = np.array([e.numpy() for e in embeddings])
        else:
            embeddings = np.array(embeddings)
        row_sums = np.sum(embeddings**2, axis=1)
        return embeddings / row_sums[:, np.newaxis]
    
    
    def embed_all_sentences(self, chains):
        """
        Embed each sentence in each chain.
        """
        all_embeddings = self.embed_sentences(
            [sentence for chain in chains for sentence in chain.chain]
        )
        index = 0
        for chain in chains:
            if len(chain.chain) == 0:
                chain.set_sentence_embeddings([[]])
            else:
                embeddings = all_embeddings[index : index + len(chain.chain)]
                chain.set_sentence_embeddings(embeddings)
            index += len(chain.chain)
    
    def embed_all_chains(self, chains: List[Chain]):
        """
        Embed each chain as a whole.
        """
        all_embeddings = self.embed_sentences(
            [". ".join(chain.chain) for chain in chains]
        )
        for chain, embedding in zip(chains, all_embeddings):
            chain.set_whole_chain_embedding(embedding)
    
    def compute_embedding_scores(
        self,
        hypo: Chain,
        context: Chain,
        # reference: Optional[Chain],
        # score_types: List[str],
        scores: Dict[str, List],
    ) -> Dict[str, List]:
        h_steps_embeddings = hypo.sentence_embeddings
        c_steps_embeddings = context.sentence_embeddings
        h_whole_chain_embedding = hypo.whole_chain_embedding
        c_whole_chain_embedding = context.whole_chain_embedding
        # Sentence Embedding Matching between context and hypos
        y_x_sent_emb = embedding_alignment(
            ref_emb=c_steps_embeddings, hypo_emb=h_steps_embeddings
        )
        x_y_sent_emb = embedding_alignment(
            ref_emb=h_steps_embeddings, hypo_emb=c_steps_embeddings
        )

        # if FAITHFUL_SENT in score_types:
        scores[FAITHFUL_SENT].append(al_mean(y_x_sent_emb))

        return scores
    
    
    def precompute_embeddings(
        self,
        hypos,
        contexts,
        # references,
    ) -> None:
        # embed all hypos using sentence embedder simultaneously
        self.embed_all_sentences(hypos)
        self.embed_all_sentences(contexts)
        self.embed_all_chains(hypos)
        self.embed_all_chains(contexts)
        # if references:
        #     self.embed_all_sentences(references)
        #     self.embed_all_chains(references)
    
    
    def evaluate(self, 
                 score_types: Optional[List[str]] = None
                ) -> Dict[str, Any]:
        """
        Score each reasoning chain.
        """
        # score_types = score_types if score_types is not None else self.score_types
        # # scores[score_type] = [score_chain1, score_chain2, ...]
        scores = defaultdict(list)

        # if contains_embedding_scores(score_types):
            # Pre-compute chain, step, and word embeddings for embedding-based metrics
        self.precompute_embeddings(
            hypos=self.hypos,
            contexts=self.context,
            # references=self.references,
        )

        for i in tqdm(range(len(self.hypos)), desc="Scoring chains ... "):
            if len(self.hypos[i].chain) == 0:
                for score in score_types:
                    scores[score].append("N/A")
                continue

            # if contains_embedding_scores(score_types):
                # Calculate all embedding-based scores
            scores = self.compute_embedding_scores(
                hypo=self.hypos[i],
                context=self.context[i],
                # reference=self.references[i] if self.references else None,
                # reference= None,
                # score_types=score_types,
                scores=scores,
            )
        
        return scores


def save_scores(score_dict: Dict, out_path: str) -> None:
    # create destination directory if not exists
    pathlib.Path(os.path.dirname(out_path)).mkdir(parents=True, exist_ok=True)
    score_list = list(score_dict.keys())
    with open(out_path, 'w') as output_file:
        n_scores = len(score_list)
        out_line = "{:<8}\t" + "\t".join(["{:<15}" for i in range(n_scores)])
        print(out_line.format('ID', *score_list), file=output_file)
        n_samples = len(score_dict[score_list[0]])
        for i in range(n_samples):
            scores = []
            for score in score_list:
                scores.append(score_dict[score][i])
            print(out_line.format(i, *scores), file=output_file)
    print(f"Scores written to {out_path}")

if __name__ == '__main__':

    dataset_path = "../dataset/gsm8k-generat-data/enhanced_data/7_time_data/train-enhanced.json"
    evaluator = ReasoningEvaluator(
        # score_types=['faithfulness'],
        model_type="sim_sce",
        transformer_model="facebook/roscoe-512-roberta-base",
        # ppl_model="gpt2-large", # no use
        # discourse_batch=64, # no use
        # coherence_batch=16, # no use
    )
    evaluator.update_evaluator(context = ["Every day, Wendi feeds each of her chickens three cups of mixed chicken feed, containing seeds, mealworms and vegetables to help keep them healthy.  She gives the chickens their feed in three separate meals. In the morning, she gives her flock of chickens 15 cups of feed.  In the afternoon, she gives her chickens another 25 cups of feed.  How many cups of feed does she need to give her chickens in the final meal of the day if the size of Wendi's flock is 20 chickens?"],
                               reasoning_code=[" # Calculate the total amount of feed needed for the day"]
                               )
            
            
    scores = evaluator.evaluate(score_types=['faithfulness'])
    # print(np.log(scores["faithfulness"]))
    
    # save 
    # out_path = "./test/scores_recor.tsv"
    # save_scores(scores, out_path)
    # score_type = (
    #     REASONING_SCORES
    #     if "esnli" in dataset_path or "gsm8k" in dataset_path
    #     else UNSUPERVISED_SCORES
    # )