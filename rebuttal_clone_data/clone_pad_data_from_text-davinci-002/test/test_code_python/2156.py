def solution():
    initial_distance = 70
    first_day = 20
    second_day = first_day / 2 - 6
    third_day = 10
    total_distance = initial_distance - (first_day + second_day + third_day)
    result = total_distance
    return result

print(solution())