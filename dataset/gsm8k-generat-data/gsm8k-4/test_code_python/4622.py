def solution():
    """Annie went to a liquidation sale and bought 5 televisions that each cost $50. She also purchased 10 figurines. If Annie spent $260 in total, how much did a single figurine cost in dollars?"""
    # Define the cost of each television and the number of televisions Annie bought
    TV_COST = 50
    NUM_TVS = 5

    # Define the total amount Annie spent and the number of figurines she bought
    total_spent = 260
    num_figurines = 10

    # Calculate the total cost of the televisions
    tv_cost_total = TV_COST * NUM_TVS

    # Calculate the total cost of the figurines
    figurine_cost_total = total_spent - tv_cost_total

    # Calculate the cost of each figurine
    figurine_cost_each = figurine_cost_total / num_figurines

    # return the result
    result = figurine_cost_each
    return result

print(solution())