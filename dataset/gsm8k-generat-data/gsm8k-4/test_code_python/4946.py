def solution():
    """There are three buckets of seeds labeled A, B, and C with 100 seeds. There are ten more seeds in bucket A than in bucket B, and bucket B has 30 seeds. How many seeds are in bucket C?"""
    # Define the number of seeds in bucket B
    bucket_b_seeds = 30

    # Calculate the number of seeds in bucket A
    bucket_a_seeds = bucket_b_seeds + 10

    # Calculate the total number of seeds in buckets A and B
    total_seeds_a_b = bucket_a_seeds + bucket_b_seeds

    # Calculate the number of seeds in bucket C
    bucket_c_seeds = 100 - total_seeds_a_b

    # return the result
    result = bucket_c_seeds
    return result

print(solution())