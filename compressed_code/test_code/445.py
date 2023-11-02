def solution():
    
    initial_tokens = 1000000
    self_tokens = initial_tokens / 2
    remaining_tokens = initial_tokens - self_tokens
    sibling_tokens = remaining_tokens / 4
    difference = self_tokens - sibling_tokens
    result = difference
    return result

print(solution())