def solution():
    
    total_distance = 120
    initial_speed = 60
    initial_time = 0.5  
    remaining_distance = total_distance - (initial_speed * initial_time)
    remaining_time = 1.5 - initial_time
    remaining_speed = remaining_distance / remaining_time
    result = remaining_speed
    return result

print(solution())