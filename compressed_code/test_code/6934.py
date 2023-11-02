def solution():
    
    total_distance = 24
    total_time = 8
    first_leg_time = 4
    first_leg_distance = 4 * 4
    second_leg_distance = total_distance - first_leg_distance
    second_leg_time = total_time - first_leg_time
    speed_needed = second_leg_distance / second_leg_time
    result = speed_needed
    return result

print(solution())