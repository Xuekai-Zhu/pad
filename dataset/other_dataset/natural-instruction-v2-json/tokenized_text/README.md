**This data use the version of natural instruction v2 on huggingface.** Note that we pretokenize all data, in form of :

* inputs = labels = (defintion + inputs + outputs)
* ```
  tokenizer = AutoTokenizer.from_pretrained("facebook/opt-2.7b")
  ```
