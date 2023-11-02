def solution():
    """Javier is selling donuts to raise money for a new game. He wants to raise $96. He buys each dozen donuts for $2.40 and then sells each donut for $1. How many dozen donuts does he need to buy and sell to reach his goal?"""
    # Define the cost and selling price of each donut
    COST_PER_DOZEN = 2.4
    SELLING_PRICE_PER_DONUT = 1

    # Define the amount of money Javier wants to raise
    GOAL = 96

    # Calculate the profit per donut
    profit_per_donut = SELLING_PRICE_PER_DONUT - COST_PER_DOZEN / 12

    # Calculate the number of donuts Javier needs to sell
    num_donuts = GOAL / profit_per_donut

    # Calculate the number of dozens Javier needs to buy
    num_dozens = num_donuts / 12

    # Round up to the nearest dozen
    num_dozens = math.ceil(num_dozens)

    # Display the number of dozens Javier needs to buy and sell
    result = num_dozens
    return result

print(solution())