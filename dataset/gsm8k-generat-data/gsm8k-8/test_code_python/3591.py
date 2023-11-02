def solution():
    # Calculate the gain in the first week
    week1_gain = 0.25 * 400

    # Calculate the value of the investment after the first week
    week1_value = 400 + week1_gain

    # Calculate the gain in the second week
    week2_gain = 0.50 * week1_value

    # Calculate the value of the investment after the second week
    total_value = week1_value + week2_gain
    result = total_value
    return result

print(solution())