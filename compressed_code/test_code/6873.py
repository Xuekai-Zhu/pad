def solution():
    
    bucket_size = 120
    filled_buckets = 14
    removed_buckets = 3
    total_water = (filled_buckets - removed_buckets) * bucket_size
    water_per_week = total_water * 7
    result = water_per_week
    return result

print(solution())