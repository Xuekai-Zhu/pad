def solution():
    # Calculate the number of tokens Sandy will keep for herself
    sandy_tokens = 1000000 / 2  

    # Calculate the number of tokens each of her siblings will receive
    sibling_tokens = sandy_tokens / 4  

    # Calculate the difference between the number of tokens Sandy has and her siblings
    token_diff = sandy_tokens - sibling_tokens  

    result = token_diff
    return result

print(solution())