def solution():
    # Number of apples picked in the first hour
    first_hour_apples = 66

    # Number of apples picked in the second hour
    second_hour_apples = 2 * first_hour_apples

    # Number of apples picked in the third hour
    third_hour_apples = first_hour_apples / 3

    # Total number of apples picked
    total_apples = first_hour_apples + second_hour_apples + third_hour_apples
    result = total_apples
    return result

print(solution())