def solution():
    # Calculate the number of apples Kylie picked in the first hour
    first_hour_apples = 66

    # Calculate the number of apples Kylie picked in the second hour, doubling her rate
    second_hour_apples = 2 * first_hour_apples

    # Calculate the number of apples Kylie picked in the third hour, picking a third of the first hour
    third_hour_apples = first_hour_apples / 3

    # Calculate the total number of apples Kylie picked
    total_apples = first_hour_apples + second_hour_apples + third_hour_apples
    result = total_apples
    return result

print(solution())