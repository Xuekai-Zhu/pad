def solution():
    """Denver uses 7 pieces of wood for each birdhouse and he pays $1.50 for each piece of wood. If he makes a $5.50 profit per birdhouse, how much will Denver charge to Danny for buying two birdhouses?"""
    # Define the cost of each piece of wood
    wood_cost = 1.5

    # Define the number of pieces of wood used for each birdhouse
    wood_per_birdhouse = 7

    # Define the profit per birdhouse
    birdhouse_profit = 5.5

    # Define the number of birdhouses being purchased
    num_birdhouses = 2

    # Calculate the cost of materials for the birdhouses
    material_cost = wood_cost * wood_per_birdhouse * num_birdhouses

    # Calculate the total profit from selling the birdhouses
    total_profit = birdhouse_profit * num_birdhouses

    # Calculate the total cost for Danny to purchase two birdhouses
    total_cost = material_cost + total_profit

    # return the result
    result = total_cost
    return result

print(solution())