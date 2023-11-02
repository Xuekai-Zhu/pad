def solution():
    total_tokens = 1000000  # Sandy bought 1 million Safe Moon tokens
    tokens_kept = total_tokens / 2  # Sandy keeps half of the tokens to herself
    tokens_per_sibling = (total_tokens - tokens_kept) / 4  # Remaining tokens divided equally among 4 siblings

    # Calculate how many more tokens Sandy has compared to any of her siblings
    difference = tokens_kept - tokens_per_sibling
    result = difference
    return result

print(solution())