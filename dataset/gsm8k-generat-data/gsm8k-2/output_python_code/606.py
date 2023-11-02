def solution():
    """Sandy bought 1 million Safe Moon tokens. She has 4 siblings. She wants to keep half of them to herself and divide the remaining tokens among her siblings. After splitting it up, how many more tokens will she have than any of her siblings?"""
    initial_tokens = 1000000
    self_tokens = initial_tokens / 2
    remaining_tokens = initial_tokens - self_tokens
    sibling_tokens = remaining_tokens / 4
    difference = self_tokens - sibling_tokens
    result = difference
    return result

print(solution())