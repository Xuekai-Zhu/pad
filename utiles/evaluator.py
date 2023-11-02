from bert_score import score, BERTScorer
import json
import numpy as np
from tqdm import tqdm
import jieba
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction, corpus_bleu
from nltk import ngrams
from nltk import word_tokenize



def load_text(file):
    hypothesis_list = []
    with open(file, 'r') as fin:
        data = fin.readlines()
        for line in data:
            item = json.loads(line)
            text = item["output"]
            hypothesis_list.append(text)
    return hypothesis_list

def load_target(file):
    hypothesis_list = []
    with open(file, 'r') as fin:
        data = fin.readlines()
        for line in data:
            item = json.loads(line)
            text = item["worker_answer"]
            hypothesis_list.append(text)
    return hypothesis_list
    

def bert_sco(cands, refs, lang):
    # os.environ["CUDA_VISIBLE_DEVICES"] = "1"
    # scorer = BERTScorer(lang="zh", rescale_with_baseline=True)
    cand_list = load_text(cands)
    refs_list = load_target(refs)
    (P, R, F), hashname = score(cand_list, refs_list, lang=lang, return_hash=True)
    print(f"{hashname}: P={P.mean().item():.6f} R={R.mean().item():.6f} F={F.mean().item():.6f}")




class Bleu_Metric(object):
    def __init__(self, hypothesis_file, reference_file, p_key, y_key):
        self.hypothesis_list = []
        self.refernce_list = []
        with open(hypothesis_file, 'r') as fin:
            data = fin.readlines()
            for line in data:
                item = json.loads(line)
                text = item[p_key]
                self.hypothesis_list.append(text)
        with open(reference_file, 'r') as fin:
            data = fin.readlines()
            for line in data:
                item = json.loads(line)
                text = item[y_key]
                self.refernce_list.append(text)

    def proline(self, line):
        return " ".join([w for w in jieba.cut("".join(line.strip().split()))])
    
    def bleu(self):
        """
        compute rouge score
        Args:
            data (list of dict including reference and candidate):
        Returns:
                res (dict of list of scores): rouge score
        """

        res = {}
        for i in range(1, 5):
            res["bleu-%d" % i] = []

        for origin_reference, origin_candidate in tqdm(zip(self.refernce_list, self.hypothesis_list)):
            # origin_candidate = tmp_data['candidate']
            # origin_reference = tmp_data['reference']
            origin_reference = self.proline(origin_reference)
            origin_candidate = self.proline(origin_candidate)
            assert isinstance(origin_candidate, str)
            if not isinstance(origin_reference, list):
                origin_reference = [origin_reference]

            for i in range(1, 5):
                res["bleu-%d" % i].append(sentence_bleu(references=[r.strip().split() for r in origin_reference],
                                                        hypothesis=origin_candidate.strip().split(),
                                                        weights=tuple([1. / i for j in range(i)])))

        for key in res:
            res[key] = np.mean(res[key])

        print(res)

        return res

    def bleu_en(self):
        res = {}
        for i in range(1, 5):
            res["bleu-%d" % i] = []

        for origin_reference, origin_candidate in tqdm(zip(self.refernce_list, self.hypothesis_list)):
            origin_candidate = word_tokenize(origin_candidate)
            origin_reference = word_tokenize(origin_reference)
            # origin_reference = proline(origin_reference)
            # origin_candidate = proline(origin_candidate)
            # assert isinstance(origin_candidate, str)
            # if not isinstance(origin_reference, list):
            #     origin_reference = [origin_reference]

            for i in range(1, 5):
                res["bleu-%d" % i].append(sentence_bleu(references=[origin_reference],
                                                        hypothesis=origin_candidate,
                                                        weights=tuple([1. / i for j in range(i)])))
        for key in res:
            res[key] = np.mean(res[key])

        print(res)

        return res

if __name__ == '__main__':
    output_file_1 = "predict/opt-2.7b/care_1000_test/base.json"
    output_file_2 = "predict/opt-2.7b/care_1000_test/base+rot.json"
    output_file_3 = "predict/opt-2.7b/care_1000_test/base+showing.json"
    output_file_4 = "predict/opt-2.7b/care_1000_test/base+sorting.json"
    reference_file = "dataset/mic/sample_1000_mic_test.json"
    
    test_files = [output_file_1, output_file_2, output_file_3, output_file_4]
    for i in test_files:
        print(i)
        bert_sco(i, reference_file, lang="en")
        bleu_score = Bleu_Metric(hypothesis_file=i, reference_file=reference_file, p_key="output", y_key="worker_answer").bleu_en()
        print("-------------------------")