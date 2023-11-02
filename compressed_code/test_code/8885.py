def solution():
    
    run_speed = 3 
    walk_speed = 1 
    run_distance = 0.5 
    walk_distance = 0.5 
    total_distance = run_distance + walk_distance 
    total_time = (run_distance / run_speed) + (walk_distance / walk_speed) 
    total_minutes = total_time * 60 
    result = total_minutes
    return result

print(solution())