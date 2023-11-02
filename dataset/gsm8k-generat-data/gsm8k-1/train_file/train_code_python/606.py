def solution():
    """Sandy bought 1 million Safe Moon tokens. She has 4 siblings. She wants to keep half of them to herself and divide the remaining tokens among her siblings. After splitting it up, how many more tokens will she have than any of her siblings?"""
    total_tokens = 1000000
    siblings = 4
    tokens_kept = total_tokens / 2
    tokens_per_sibling = (total_tokens - tokens_kept) / siblings
    difference = tokens_kept - tokens_per_sibling
    result = difference
    return result

print(solution())