def solution():
    """John buys 3 t-shirts that cost $20 each. He also buys $50 in pants. How much does he spend?"""
    # Define the cost of each t-shirt and the cost of pants
    TSHIRT_COST = 20
    PANTS_COST = 50

    # Calculate the total cost of the t-shirts
    tshirt_total_cost = TSHIRT_COST * 3

    # Calculate the total cost of the purchase
    total_cost = tshirt_total_cost + PANTS_COST

    result = total_cost
    return result

print(solution())