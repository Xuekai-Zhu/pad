def solution():
    
    
    walk_distance = 3
    walk_speed = 3
    walk_time = walk_distance / walk_speed
    
    
    run_distance = 10
    run_speed = 5
    run_time = run_distance / run_speed
    
    
    total_time = walk_time + run_time
    
    
    days_per_week = 7
    time_per_week = total_time * days_per_week
    
    result = time_per_week
    return result

print(solution())