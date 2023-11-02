def solution():
    """Maria's birthday is in 22 days. Her friend Lilly wants to buy her flowers so she saves $2 each day until Maria's birthday. If a flower costs $4, how many flowers can she buy?"""
    # Define the number of days and the cost of a flower
    DAYS = 22
    FLOWER_COST = 4

    # Initialize the savings counter and the number of flowers
    savings = 0
    num_flowers = 0

    # Calculate the total savings and the number of flowers that can be bought
    for i in range(DAYS):
        savings += 2
        if savings >= FLOWER_COST:
            num_flowers += 1
            savings -= FLOWER_COST

    # Return the result
    result = num_flowers
    return result

print(solution())