def solution():
    # Number of seeds in bucket A
    seeds_A = 30 + 10  # Bucket A has 10 more seeds than bucket B

    # Total number of seeds in buckets A and B
    total_seeds_A_B = seeds_A + 30  # Bucket B has 30 seeds

    # Number of seeds in bucket C
    seeds_C = 100 - total_seeds_A_B

    result = seeds_C
    return result

print(solution())