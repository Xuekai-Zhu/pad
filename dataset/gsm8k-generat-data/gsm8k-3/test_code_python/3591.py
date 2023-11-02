def solution():
    """Pima invested $400 in Ethereum. In the first week, it gained 25% in value. In the second week, it gained an additional 50% on top of the previous gain. How much is her investment worth now?"""
    # Define the initial investment amount
    initial_investment = 400

    # Calculate the new value after the first week's gain
    first_week_gain = 0.25
    value_after_first_week = initial_investment * (1 + first_week_gain)

    # Calculate the new value after the second week's gain
    second_week_gain = 0.5
    value_after_second_week = value_after_first_week * (1 + second_week_gain)

    # Display the final value of the investment
    result = value_after_second_week
    return result

print(solution())