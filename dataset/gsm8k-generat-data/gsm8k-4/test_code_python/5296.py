def solution():
    """Bob orders a dozen muffins a day for $0.75 each and sells them for $1.5 each. How much profit does he make a week?"""
    # Define the price and cost of each muffin
    MUFFIN_COST = 0.75
    MUFFIN_PRICE = 1.5

    # Calculate the profit for one muffin
    muffin_profit = MUFFIN_PRICE - MUFFIN_COST

    # Calculate the profit for one dozen muffins
    dozen_profit = muffin_profit * 12

    # Calculate the profit for one day of selling dozen muffins
    daily_profit = dozen_profit * 1

    # Calculate the profit for one week of selling dozen muffins
    weekly_profit = daily_profit * 7

    # return the result
    result = weekly_profit
    return result

print(solution())