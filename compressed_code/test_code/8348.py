def solution():
    
    uphill_speed = 9
    downhill_speed = 12
    hill_height = 900
    uphill_time = hill_height / uphill_speed
    downhill_time = hill_height / downhill_speed
    total_time = uphill_time + downhill_time
    result = total_time
    return result

print(solution())