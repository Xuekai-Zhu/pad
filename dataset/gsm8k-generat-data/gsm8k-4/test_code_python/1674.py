def solution():
    """John buys 1.5 ounces of silver and twice as much gold. The silver costs $20 per ounce. The gold is 50 times more expensive per ounce. How much does he spend on everything?"""
    # Define the cost of silver and the amount purchased
    silver_cost = 20
    silver_amount = 1.5

    # Define the cost and amount of gold
    gold_cost = silver_cost * 50
    gold_amount = silver_amount * 2

    # Calculate the total cost of silver and gold
    total_cost = (silver_amount * silver_cost) + (gold_amount * gold_cost)

    # return the result
    result = total_cost
    return result

print(solution())