def solution():
    """There are three buckets of seeds labeled A, B, and C with 100 seeds. There are ten more seeds in bucket A than in bucket B, and bucket B has 30 seeds. How many seeds are in bucket C?"""
    seeds_in_bucket_b = 30
    seeds_in_bucket_a = seeds_in_bucket_b + 10
    total_seeds_in_a_and_b = seeds_in_bucket_a + seeds_in_bucket_b
    seeds_in_bucket_c = 100 - total_seeds_in_a_and_b
    result = seeds_in_bucket_c
    return result

print(solution())