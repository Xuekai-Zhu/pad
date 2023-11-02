def solution():
    total_distance = 6
    first_distance = 3
    second_distance = 2
    third_distance = 1
    first_speed = 150
    second_speed = first_speed + 50
    third_speed = first_speed * 2
    average_speed = (first_speed * first_distance + second_speed * second_distance + third_speed * third_distance) / total_distance
    result = average_speed
    return result

print(solution())