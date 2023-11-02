def solution():
    """Ben bought a lawnmower for his garden. He paid $100 for it. After six months, the value of the mower dropped by about 25%. Over the next year, the value of the mower dropped another 20% in value. How much is Ben's lawnmower worth after this time?"""

    # Define the initial price and the percentage decrease in the first 6 months
    initial_price = 100
    first_decrease = 0.25

    # Calculate the price after the first decrease
    price_after_6_months = initial_price * (1 - first_decrease)

    # Define the percentage decrease in the next year
    second_decrease = 0.2

    # Calculate the price after the second decrease
    price_after_18_months = price_after_6_months * (1 - second_decrease)

    result = price_after_18_months
    return result

print(solution())