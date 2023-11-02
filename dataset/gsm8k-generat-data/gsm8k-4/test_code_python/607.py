def solution():
    """Sandy bought 1 million Safe Moon tokens. She has 4 siblings. She wants to keep half of them to herself and divide the remaining tokens among her siblings. After splitting it up, how many more tokens will she have than any of her siblings?"""
    # Define the number of tokens Sandy bought
    total_tokens = 1000000

    # Keep half of the tokens, and divide the remaining among her siblings
    shared_tokens = total_tokens // 2
    tokens_per_sibling = shared_tokens // 4

    # Calculate the number of tokens Sandy will have left after splitting
    sandy_tokens_left = shared_tokens % 4 + tokens_per_sibling

    # Calculate the difference between Sandy's tokens and her siblings' tokens
    diff = sandy_tokens_left - tokens_per_sibling

    result = diff
    return result

print(solution())