def solution():
    
    bucket_b_seeds = 30
    bucket_a_seeds = bucket_b_seeds + 10
    total_seeds = 100
    bucket_c_seeds = total_seeds - bucket_a_seeds - bucket_b_seeds
    result = bucket_c_seeds
    return result

print(solution())