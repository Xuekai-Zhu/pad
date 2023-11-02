def solution():
    
    first_leg_speed = 80
    first_leg_time = 6
    first_leg_distance = first_leg_speed * first_leg_time

    second_leg_speed = 60
    second_leg_time = 4
    second_leg_distance = second_leg_speed * second_leg_time

    third_leg_speed = 40
    third_leg_time = 2
    third_leg_distance = third_leg_speed * third_leg_time

    total_distance = first_leg_distance + second_leg_distance + third_leg_distance
    result = total_distance
    return result

print(solution())