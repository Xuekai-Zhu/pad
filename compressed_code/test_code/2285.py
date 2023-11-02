def solution():
    
    speed = 30
    uphill_speed = 0.5 * speed
    downhill_speed = 1.2 * speed
    uphill_distance = 60
    downhill_distance = 72
    uphill_time = uphill_distance / uphill_speed
    downhill_time = downhill_distance / downhill_speed
    total_time = uphill_time + downhill_time
    result = total_time
    return result

print(solution())