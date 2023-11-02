def solution():
    
    shark_buckets = 4
    dolphin_buckets = shark_buckets / 2
    other_buckets = shark_buckets * 5
    total_buckets = shark_buckets + dolphin_buckets + other_buckets
    weeks = 546 / total_buckets / 7
    result = weeks
    return result

print(solution())