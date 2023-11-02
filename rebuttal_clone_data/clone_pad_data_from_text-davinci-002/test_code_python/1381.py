def solution():
    buckets_to_fill = 14
    buckets_to_empty = 3
    bucket_size = 120
    total_ounces = (buckets_to_fill - buckets_to_empty) * bucket_size
    ounces_per_day = total_ounces / 7
    result = ounces_per_day
    
    return result

print(solution())