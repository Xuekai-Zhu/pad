def solution():
    # Calculate the total number of apples picked by Kylie
    first_hour_apples = 66  # number of apples picked in the first hour
    second_hour_apples = 2 * 66  # number of apples picked in the second hour (double the rate of the first hour)
    third_hour_apples = 1/3 * 66  # number of apples picked in the third hour (one-third of the first hour)
    total_apples = first_hour_apples + second_hour_apples + third_hour_apples  # sum of apples picked in all three hours
    result = total_apples
    return result

print(solution())