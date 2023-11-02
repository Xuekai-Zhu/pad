def solution():
    initial_investment = 400
    first_week_gain = 0.25 # 25% gain
    second_week_gain = 0.5 # 50% gain

    # Calculate the value after the first week
    first_week_value = initial_investment * (1 + first_week_gain)

    # Calculate the value after the second week
    second_week_value = first_week_value * (1 + second_week_gain)

    result = second_week_value
    return result

print(solution())