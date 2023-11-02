def solution():
    """Ben bought a lawnmower for his garden. He paid $100 for it. After six months, the value of the mower dropped by about 25%. Over the next year, the value of the mower dropped another 20% in value. How much is Ben's lawnmower worth after this time?"""
    # Define the initial cost of the lawnmower
    initial_cost = 100

    # Calculate the value of the lawnmower after the first 6 months
    six_month_value = initial_cost * 0.75

    # Calculate the value of the lawnmower after another year
    one_year_value = six_month_value * 0.8

    # Display the final value of the lawnmower
    result = one_year_value
    return result

print(solution())