def solution():
    
    caleb_bucket_size = 7
    cynthia_bucket_size = 8
    pool_size = 105
    total_trips_needed = pool_size / (caleb_bucket_size + cynthia_bucket_size)
    result = total_trips_needed
    return result

print(solution())