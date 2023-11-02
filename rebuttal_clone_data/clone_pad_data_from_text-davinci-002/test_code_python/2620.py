def solution():
     start_tokens = 36
     spent_tokens = start_tokens / 3 + start_tokens / 4 + 7
     bought_tokens = 7 * 7
     end_tokens = start_tokens - spent_tokens + bought_tokens
     result = end_tokens
     return result

print(solution())