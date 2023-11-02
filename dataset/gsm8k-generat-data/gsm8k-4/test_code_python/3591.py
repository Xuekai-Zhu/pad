def solution():
    """Pima invested $400 in Ethereum. In the first week, it gained 25% in value. In the second week, it gained an additional 50% on top of the previous gain. How much is her investment worth now?"""
    # Define the initial investment
    investment = 400

    # Calculate the value of the investment after the first week
    week_one_profit = investment * 0.25
    week_one_value = investment + week_one_profit

    # Calculate the value of the investment after the second week
    week_two_profit = week_one_value * 0.5
    week_two_value = week_one_value + week_two_profit

    # return the result
    result = week_two_value
    return result

print(solution())