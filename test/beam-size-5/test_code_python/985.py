def solution():
    
    peel_shrimp_per_minute = 6
    saute_shrimp_per_minute = 30
    total_shrimp = 90
    time_to_peel = total_shrimp / peel_shrimp_per_minute
    time_to_saute = time_to_peel / saute_shrimp_per_minute
    total_time = time_to_peel + time_to_saute
    result = total_time
    return result

print(solution())