def solution():
    
    initial_speed = 30
    top_distance = 60
    bottom_distance = 72
    uphill_speed = initial_speed * 0.5
    downhill_speed = initial_speed * 1.2
    time_uphill = top_distance / uphill_speed
    time_downhill = bottom_distance / downhill_speed
    total_time = time_uphill + time_downhill
    result = total_time
    return result

print(solution())