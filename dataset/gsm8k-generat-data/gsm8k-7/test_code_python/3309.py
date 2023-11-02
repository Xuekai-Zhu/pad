def solution():
    pieces_per_birdhouse = 7
    cost_per_piece = 1.5
    profit_per_birdhouse = 5.5
    num_birdhouses = 2

    # Calculate the total cost of all pieces of wood needed
    total_wood_cost = pieces_per_birdhouse * num_birdhouses * cost_per_piece

    # Calculate the total profit from selling the birdhouses
    total_profit = num_birdhouses * profit_per_birdhouse

    # Calculate the total cost of the birdhouses, including the cost of wood
    total_cost = total_wood_cost + total_profit

    # Divide the total cost by the number of birdhouses to get the cost per birdhouse
    cost_per_birdhouse = total_cost / num_birdhouses

    # Double the cost per birdhouse to get the cost for two birdhouses
    result = cost_per_birdhouse * 2
    return result

print(solution())