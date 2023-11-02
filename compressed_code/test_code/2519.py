def solution():
    
    uphill_speed = 9
    downhill_speed = 12
    hill_distance = 900
    uphill_time = hill_distance / uphill_speed
    downhill_time = hill_distance / downhill_speed
    total_time = uphill_time + downhill_time
    result = total_time
    return result

print(solution())