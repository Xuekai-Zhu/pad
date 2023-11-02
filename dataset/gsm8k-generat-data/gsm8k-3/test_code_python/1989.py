def solution():
    """Yulia was able to net $44 in profit this week. Her lemonade stand made a gross revenue of $47 this week. She was also able to babysit and made $31. However, her lemonade stand is expensive to run because she needs to buy lemons, sugar, and sunscreen. How much did she spend to operate her lemonade stand, in dollars?"""
    # Define the gross revenue and profit for the week
    GROSS_REVENUE = 47
    NET_PROFIT = 44
    BABYSITTING_EARNINGS = 31

    # Calculate the cost of operating the lemonade stand
    LEMON_COST = 5
    SUGAR_COST = 3
    SUNSCREEN_COST = 2
    OPERATING_COSTS = LEMON_COST + SUGAR_COST + SUNSCREEN_COST
    LEMONADE_STAND_COST = GROSS_REVENUE - (NET_PROFIT + BABYSITTING_EARNINGS) - OPERATING_COSTS

    # Display the cost of operating the lemonade stand
    result = LEMONADE_STAND_COST
    return result

print(solution())