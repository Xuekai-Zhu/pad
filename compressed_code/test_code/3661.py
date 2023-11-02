def solution():
    
    run_time = 5
    swing_time = 10
    run_speed = 15
    swing_speed = 10
    run_distance = run_time * run_speed
    swing_distance = swing_time * swing_speed
    total_distance = run_distance + swing_distance
    result = total_distance
    return result

print(solution())