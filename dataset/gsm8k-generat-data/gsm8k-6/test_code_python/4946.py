def solution():
    # Calculate the number of seeds in bucket A
    seeds_A = 30 + 10  # There are ten more seeds in bucket A than in bucket B

    # Calculate the total number of seeds in all three buckets
    total_seeds = seeds_A + 30 + 100  # Buckets A, B, and C each have 100 seeds

    # Calculate the number of seeds in bucket C
    seeds_C = total_seeds - seeds_A - 30

    result = seeds_C
    return result

print(solution())