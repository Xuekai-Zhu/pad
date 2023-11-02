def solution():
    # Calculate the cost of materials for one birdhouse
    cost_per_piece = 1.5
    pieces_per_birdhouse = 7
    material_cost = cost_per_piece * pieces_per_birdhouse

    # Calculate the total profit for one birdhouse
    profit_per_birdhouse = 5.5

    # Calculate the total cost and profit for two birdhouses
    total_material_cost = material_cost * 2
    total_profit = profit_per_birdhouse * 2

    # Calculate the total cost for two birdhouses, including profit
    total_cost = total_material_cost + total_profit

    # Divide the total cost by 2, since Danny is buying two birdhouses
    final_cost = total_cost / 2
    result = final_cost
    return result

print(solution())