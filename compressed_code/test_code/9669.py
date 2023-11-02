def solution():
    
    seeds_in_bucket_b = 30
    seeds_in_bucket_a = seeds_in_bucket_b + 10
    total_seeds_in_a_and_b = seeds_in_bucket_a + seeds_in_bucket_b
    seeds_in_bucket_c = 100 - total_seeds_in_a_and_b
    result = seeds_in_bucket_c
    return result

print(solution())