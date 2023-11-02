def solution():
    initial_investment = 400  # Pima invested $400 in Ethereum
    first_week_gain = 0.25  # Ethereum gained 25% in the first week
    second_week_gain = 0.5  # Ethereum gained an additional 50% on top of the previous gain in the second week

    # Calculate the value of the investment after the first week
    value_after_first_week = initial_investment + (first_week_gain * initial_investment)

    # Calculate the value of the investment after the second week
    value_after_second_week = value_after_first_week + (second_week_gain * value_after_first_week)

    result = value_after_second_week
    return result

print(solution())