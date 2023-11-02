def solution():
    first_hour_apples = 66
    second_hour_apples = 2 * first_hour_apples
    third_hour_apples = first_hour_apples / 3

    total_apples = first_hour_apples + second_hour_apples + third_hour_apples
    result = total_apples
    return result

print(solution())