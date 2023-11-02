def solution():
    """The pet store can buy a goldfish for $.25 and sell it for $.75. The owner plans to use the profits from goldfish sales to buy a new tank, which costs $100. After one week, he is 45% short of the price. How many goldfish did he sell that week?"""
    # Define the cost and selling price of a goldfish
    COST_PRICE = 0.25
    SELLING_PRICE = 0.75

    # Define the price of the new tank
    TANK_PRICE = 100

    # Calculate the profit per goldfish
    PROFIT_PER_GOLDFISH = SELLING_PRICE - COST_PRICE

    # Calculate the number of goldfish needed to buy the tank
    goldfish_needed = TANK_PRICE / PROFIT_PER_GOLDFISH

    # Calculate the number of goldfish sold after one week
    percent_short = 0.45
    goldfish_sold = goldfish_needed / (1 - percent_short)

    # Round and return the result
    result = round(goldfish_sold)
    return result

print(solution())