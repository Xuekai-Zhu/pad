def solution():
    tokens = 1000000
    siblings = 4
    
    # Calculate the number of tokens Sandy keeps for herself
    sandy_tokens = tokens / 2
    
    # Calculate the number of tokens each sibling gets
    sibling_tokens = (tokens - sandy_tokens) / siblings
    
    # Calculate the difference between Sandy's tokens and each sibling's tokens
    difference = sandy_tokens - sibling_tokens
    
    result = difference
    return result

print(solution())