def solution():
    # Find which two buckets were poured into the first large bucket
    possible_pairs = [(11,13), (11,12), (11,16), (13,12), (13,16), (12,16)]
    first_large_bucket = 23
    for pair in possible_pairs:
        if sum(pair) == first_large_bucket:
            smaller_bucket = min(pair)
            larger_bucket = max(pair)

    # Find the total amount of water in the second large bucket
    remaining_buckets_total = 11 + 13 + 12 + 16 - smaller_bucket - larger_bucket
    result = remaining_buckets_total
    return result

print(solution())