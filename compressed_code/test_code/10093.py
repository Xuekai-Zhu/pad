def solution():
    
    bucket_size = 2
    time_to_fill_bucket = 20
    pool_size = 84
    buckets_to_fill_pool = pool_size / bucket_size
    time_to_fill_pool_in_seconds = buckets_to_fill_pool * time_to_fill_bucket
    time_to_fill_pool_in_minutes = time_to_fill_pool_in_seconds / 60
    result = time_to_fill_pool_in_minutes
    return result

print(solution())