def solution():
    
    run_speed = 3
    walk_speed = 1
    run_distance = 0.5
    walk_distance = 0.5
    run_time = run_distance / run_speed
    walk_time = walk_distance / walk_speed
    total_time = run_time + walk_time
    result = total_time * 60
    return result

print(solution())