def solution():
    """Annie went to a liquidation sale and bought 5 televisions that each cost $50. She also purchased 10 figurines. If Annie spent $260 in total, how much did a single figurine cost in dollars?"""
    # Define the cost of each television
    TV_COST = 50

    # Define the number of televisions purchased
    num_tvs = 5

    # Define the total cost of the televisions
    tv_cost = TV_COST * num_tvs

    # Calculate the cost of the figurines
    figurine_cost = 260 - tv_cost

    # Calculate the cost of a single figurine
    single_figurine_cost = figurine_cost / 10

    # Display the cost of a single figurine
    result = single_figurine_cost
    return result

print(solution())