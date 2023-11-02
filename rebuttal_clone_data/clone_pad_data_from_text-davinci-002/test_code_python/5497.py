def solution():
    pool_size = 84
    bucket_size = 2
    fill_time = 20
    carry_time = 60
    total_time = fill_time + carry_time
    buckets_needed = pool_size / bucket_size
    minutes_needed = buckets_needed * total_time
    result = minutes_needed
    return result

print(solution())