def solution():
    
    first_leg_time = 1.5
    first_leg_speed = 60
    first_leg_distance = first_leg_time * first_leg_speed
    second_leg_time = 2
    second_leg_speed = 45
    second_leg_distance = second_leg_time * second_leg_speed
    total_distance = first_leg_distance + second_leg_distance
    result = total_distance
    return result

print(solution())