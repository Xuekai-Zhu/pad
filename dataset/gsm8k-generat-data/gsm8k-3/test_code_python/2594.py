def solution():
    """John plays paintball 3 times a month. Each time he plays he buys 3 boxes of paintballs. They cost $25 per box. How much does he spend a month on paintballs?"""
    # Define the number of times John plays per month and the cost of each box of paintballs
    GAMES_PER_MONTH = 3
    COST_PER_BOX = 25

    # Calculate the total cost of paintballs for the month
    total_cost = GAMES_PER_MONTH * 3 * COST_PER_BOX

    # Display the total cost
    result = total_cost
    return result

print(solution())