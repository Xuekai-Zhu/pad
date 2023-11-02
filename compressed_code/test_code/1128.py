def solution():
    
    total_distance = 24
    total_time = 8
    first_leg_distance = 4 * 4
    second_leg_distance = total_distance - first_leg_distance
    second_leg_time = total_time - 4
    second_leg_speed = second_leg_distance / second_leg_time
    result = second_leg_speed
    return result

print(solution())