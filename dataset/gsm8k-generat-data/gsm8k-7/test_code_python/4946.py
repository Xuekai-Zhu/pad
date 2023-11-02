def solution():
    num_seeds_bucket_b = 30
    
    # Calculate the number of seeds in bucket A
    num_seeds_bucket_a = num_seeds_bucket_b + 10
    
    # Calculate the total number of seeds in buckets A and B
    total_seeds_a_b = num_seeds_bucket_a + num_seeds_bucket_b
    
    # Calculate the number of seeds in bucket C by subtracting the total from the total seeds available
    num_seeds_bucket_c = 100 - total_seeds_a_b
    
    result = num_seeds_bucket_c
    return result

print(solution())