def solution():
    """John pays for half the cost of raising a child. It cost $10,000 a year for the first 8 years and then twice that much per year until the child is 18. University tuition then costs $250,000. How much did it cost?"""
    # Calculate the cost of raising the child for the first 8 years
    years_1to8 = 8
    cost_1to8 = years_1to8 * 10000

    # Calculate the cost of raising the child from years 9 to 18
    years_9to18 = 10
    cost_9to18 = years_9to18 * 2 * 10000

    # Calculate the total cost of raising the child
    total_cost = cost_1to8 + cost_9to18 + 250000

    # Calculate John's share of the cost
    john_share = total_cost / 2

    result = john_share
    return result

print(solution())