def solution():
    total_distance = 10
    first_portion = 3
    second_portion = 3
    third_portion = 4
    first_speed = 6
    second_speed = 3
    third_speed = 8
    first_time = first_portion / first_speed
    second_time = second_portion / second_speed
    third_time = third_portion / third_speed
    total_time = first_time + second_time + third_time
    result = total_time
    return result

print(solution())