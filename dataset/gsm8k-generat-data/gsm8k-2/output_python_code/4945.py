def solution():
    """There are three buckets of seeds labeled A, B, and C with 100 seeds. There are ten more seeds in bucket A than in bucket B, and bucket B has 30 seeds. How many seeds are in bucket C?"""
    bucket_b_seeds = 30
    bucket_a_seeds = bucket_b_seeds + 10
    total_seeds = 100
    bucket_c_seeds = total_seeds - bucket_a_seeds - bucket_b_seeds
    result = bucket_c_seeds
    return result

print(solution())