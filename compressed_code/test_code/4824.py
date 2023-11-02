def solution():
    
    run_speed = 6 / 60  
    run_time = 20
    run_distance = run_speed * run_time
    walk_speed = 2 / 60  
    walk_time = 30
    walk_distance = walk_speed * walk_time
    total_distance = run_distance + walk_distance
    result = total_distance
    return result

print(solution())