def solution():
    
    total_tokens = 1000000
    siblings = 4
    tokens_kept = total_tokens / 2
    tokens_per_sibling = (total_tokens - tokens_kept) / siblings
    difference = tokens_kept - tokens_per_sibling
    result = difference
    return result

print(solution())