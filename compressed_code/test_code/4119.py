def solution():
    
    weekly_distance = 3500
    daily_distance = weekly_distance / 7
    loop_distance = 50
    loops_per_day = daily_distance / loop_distance
    result = loops_per_day
    return result

print(solution())