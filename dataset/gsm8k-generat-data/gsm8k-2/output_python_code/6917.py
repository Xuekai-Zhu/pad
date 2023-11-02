def solution():
    """Jennifer's boyfriend left 5 texts about the grocery shopping, 5 times more texts asking why she wasn't responding,
    and a number of texts equal to 10% of all the texts he sent previously saying he was calling the police. How many
    texts did he send total?"""
    grocery_texts = 5
    response_texts = 5 * grocery_texts
    police_texts = 0.1 * (grocery_texts + response_texts)
    total_texts = grocery_texts + response_texts + police_texts
    result = total_texts
    return result

print(solution())