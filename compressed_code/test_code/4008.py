def solution():
    
    jenny_speed = 15
    anna_speed = 45
    time_difference = 0.5  
    distance_jenny_covered = jenny_speed * time_difference
    total_distance = distance_jenny_covered
    anna_time = total_distance / anna_speed * 60  
    result = anna_time
    return result

print(solution())