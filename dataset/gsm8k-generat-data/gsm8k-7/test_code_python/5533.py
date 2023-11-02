def solution():
    num_acres = 4
    cost_per_acre = 1863
    num_lots = 9

    # Calculate the total cost of the land
    total_cost = num_acres * cost_per_acre

    # Calculate the cost per lot
    cost_per_lot = total_cost / num_lots

    result = cost_per_lot
    return result

print(solution())