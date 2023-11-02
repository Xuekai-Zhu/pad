def solution():
    
    hallway_length = 16
    father_speed = 3
    son_speed = 1
    total_speed = father_speed + son_speed
    time_to_meet = hallway_length / total_speed
    distance_from_father_end = father_speed * time_to_meet
    result = distance_from_father_end
    return result

print(solution())