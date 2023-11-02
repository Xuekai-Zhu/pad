def solution():
    # Calculate cost and profit per birdhouse
    cost_per_birdhouse = 7 * 1.50  # cost of 7 pieces of wood
    profit_per_birdhouse = 5.50

    # Calculate total cost and profit for two birdhouses
    total_cost = cost_per_birdhouse * 2
    total_profit = profit_per_birdhouse * 2

    # Calculate the total amount charged to Danny for two birdhouses
    total_price = total_cost + total_profit
    result = total_price
    return result

print(solution())