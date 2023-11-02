def solution():
    
    total_time = 8
    first_half_time = total_time / 2
    second_half_time = total_time / 2
    first_half_speed = 70
    second_half_speed = 85
    first_half_distance = first_half_time * first_half_speed
    second_half_distance = second_half_time * second_half_speed
    total_distance = first_half_distance + second_half_distance
    result = total_distance
    return result

print(solution())