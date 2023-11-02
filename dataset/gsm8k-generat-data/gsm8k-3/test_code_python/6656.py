def solution():
    """The pet store can buy a goldfish for $.25 and sell it for $.75. The owner plans to use the profits from goldfish sales to buy a new tank, which costs $100. After one week, he is 45% short of the price. How many goldfish did he sell that week?"""
    # Define the cost and selling price of the goldfish
    COST_PRICE = 0.25
    SELLING_PRICE = 0.75

    # Define the cost of the new tank
    TANK_COST = 100

    # Calculate the profit per goldfish
    profit_per_fish = SELLING_PRICE - COST_PRICE

    # Calculate the number of goldfish needed to buy the tank
    goldfish_needed = TANK_COST / profit_per_fish

    # Calculate the number of goldfish sold
    goldfish_sold = goldfish_needed / 0.55

    # Display the number of goldfish sold
    result = goldfish_sold
    return result

print(solution())