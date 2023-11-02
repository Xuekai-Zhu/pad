def solution():
    sandys_tokens = 1000000
    siblings = 4
    sandys_tokens_kept = sandys_tokens / 2
    sandys_tokens_shared = sandys_tokens - sandys_tokens_kept
    sandys_tokens_per_sibling = sandys_tokens_shared / siblings
    sandys_tokens_remaining = sandys_tokens_kept + sandys_tokens_per_sibling
    result = sandys_tokens_remaining - sandys_tokens_per_sibling
    return result

print(solution())