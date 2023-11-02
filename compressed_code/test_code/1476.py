def solution():
    
    total_distance = 200
    first_leg_distance = total_distance / 4
    first_leg_time = 1
    lunch_time = 1
    second_leg_distance = total_distance - first_leg_distance
    second_leg_time = (second_leg_distance / first_leg_distance) * first_leg_time
    total_time = first_leg_time + lunch_time + second_leg_time
    result = total_time
    return result

print(solution())