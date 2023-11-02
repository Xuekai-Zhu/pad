def solution():
    """For football season, Zachary wants to buy a new football, a pair of shorts, and a pair of football shoes. The ball costs $3.75, the shorts cost $2.40, and the shoes cost $11.85. Zachary has $10. How much more money does Zachary need?"""
    # Define the cost of each item
    FOOTBALL_COST = 3.75
    SHORTS_COST = 2.40
    SHOES_COST = 11.85

    # Define the amount of money Zachary has
    ZACHARY_MONEY = 10

    # Calculate the total cost of all the items
    total_cost = FOOTBALL_COST + SHORTS_COST + SHOES_COST

    # Calculate how much more money Zachary needs
    extra_money = total_cost - ZACHARY_MONEY

    # Display how much more money Zachary needs
    result = extra_money
    return result

print(solution())