def solution():
    """Denver uses 7 pieces of wood for each birdhouse and he pays $1.50 for each piece of wood. If he makes a $5.50 profit per birdhouse, how much will Denver charge to Danny for buying two birdhouses?"""
    # Define the cost of each piece of wood
    WOOD_COST = 1.5

    # Define the number of pieces of wood needed for each birdhouse
    wood_per_birdhouse = 7

    # Define the profit per birdhouse
    profit_per_birdhouse = 5.5

    # Calculate the cost of the wood for two birdhouses
    wood_cost = wood_per_birdhouse * 2 * WOOD_COST

    # Calculate the total profit for two birdhouses
    total_profit = profit_per_birdhouse * 2

    # Calculate the price of two birdhouses
    price = wood_cost + total_profit

    # Display the price of two birdhouses
    result = price
    return result

print(solution())