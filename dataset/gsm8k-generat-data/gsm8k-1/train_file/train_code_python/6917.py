def solution():
    """Jennifer's boyfriend left 5 texts about the grocery shopping, 5 times more texts asking why she wasn't responding, and a number of texts equal to 10% of all the texts he sent previously saying he was calling the police. How many texts did he send total?"""
    grocery_text = 5
    not_responding_text = 5 * grocery_text
    police_text = int(0.1 * (grocery_text + not_responding_text))
    total_text = grocery_text + not_responding_text + police_text
    result = total_text
    return result

print(solution())