def solution():
    
    shark_buckets = 4
    dolphin_buckets = shark_buckets / 2
    other_buckets = shark_buckets * 5
    total_buckets_per_day = shark_buckets + dolphin_buckets + other_buckets
    total_weeks = 546 / (total_buckets_per_day * 7)
    result = total_weeks
    return result

print(solution())