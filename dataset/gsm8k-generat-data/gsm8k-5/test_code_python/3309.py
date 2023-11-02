def solution():
    wood_per_birdhouse = 7  # Denver uses 7 pieces of wood for each birdhouse
    cost_per_piece_of_wood = 1.5  # Denver pays $1.50 for each piece of wood
    profit_per_birdhouse = 5.5  # Denver makes a $5.50 profit per birdhouse
    birdhouses_sold = 2  # Danny wants to buy two birdhouses

    # Calculate the total cost of materials for two birdhouses
    total_wood_cost = wood_per_birdhouse * cost_per_piece_of_wood * birdhouses_sold

    # Calculate the total profit for two birdhouses
    total_profit = profit_per_birdhouse * birdhouses_sold

    # Calculate the total amount Denver should charge Danny for two birdhouses
    total_cost = total_wood_cost + total_profit
    result = total_cost
    return result

print(solution())