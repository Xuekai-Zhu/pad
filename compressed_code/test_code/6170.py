def solution():
    
    first_leg_time = 0.5
    first_leg_speed = 30
    second_leg_time = 2 * first_leg_time
    second_leg_speed = 2 * first_leg_speed

    
    first_leg_distance = first_leg_time * first_leg_speed

    
    second_leg_distance = second_leg_time * second_leg_speed

    
    total_distance = first_leg_distance + second_leg_distance

    result = total_distance
    return result

print(solution())