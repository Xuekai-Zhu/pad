def solution():
    
    downhill_distance = 20
    downhill_speed = 5
    uphill_distance = 12
    uphill_speed = 3
    uphill_break_time = 1
    downhill_time = downhill_distance / downhill_speed
    uphill_time = uphill_distance / uphill_speed + uphill_break_time
    faster_time = min(downhill_time, uphill_time)
    slower_time = max(downhill_time, uphill_time)
    time_difference = slower_time - faster_time
    result = time_difference
    return result

print(solution())