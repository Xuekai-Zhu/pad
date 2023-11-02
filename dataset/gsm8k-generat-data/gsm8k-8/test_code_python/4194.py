def solution():
    # Calculate the total number of apples in 3 boxes
    total_apples = 14 * 3

    # Calculate the number of apples eaten per week by Henry and his brother
    weekly_apples = 2 * 7 * 3

    # Calculate the number of weeks they can spend eating the apples
    weeks = total_apples // weekly_apples
    result = weeks
    return result

print(solution())