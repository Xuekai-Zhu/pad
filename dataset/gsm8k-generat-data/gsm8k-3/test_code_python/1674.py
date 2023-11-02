def solution():
    """John buys 1.5 ounces of silver and twice as much gold.  The silver costs $20 per ounce.  The gold is 50 times more expensive per ounce.  How much does he spend on everything?"""
    # Define the cost and amount of silver purchased
    SILVER_COST = 20
    SILVER_AMOUNT = 1.5

    # Define the cost and amount of gold purchased
    GOLD_COST = SILVER_COST * 50
    GOLD_AMOUNT = SILVER_AMOUNT * 2

    # Calculate the total cost of the silver
    silver_total_cost = SILVER_COST * SILVER_AMOUNT

    # Calculate the total cost of the gold
    gold_total_cost = GOLD_COST * GOLD_AMOUNT

    # Calculate the total cost of everything
    total_cost = silver_total_cost + gold_total_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())