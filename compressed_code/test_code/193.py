def solution():
    
    days_per_week = 3
    lifting_time_per_day = 1
    warmup_time_per_day = lifting_time_per_day / 3
    total_time_per_day = lifting_time_per_day + warmup_time_per_day
    total_time_per_week = total_time_per_day * days_per_week
    result = total_time_per_week
    return result

print(solution())