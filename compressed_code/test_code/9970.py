def solution():
    
    total_meters_per_week = 3500
    meters_per_loop = 50
    loops_per_day = total_meters_per_week / (meters_per_loop * 7)
    result = loops_per_day
    return result

print(solution())