def solution():
    num_shirts = 10  # James buys 10 shirts
    num_pants = num_shirts / 2  # James buys half as many pants as shirts
    cost_shirt = 6  # Each shirt costs $6
    cost_pants = 8  # Each pant costs $8

    # Calculate the total cost of the shirts
    total_cost_shirt = num_shirts * cost_shirt

    # Calculate the total cost of the pants
    total_cost_pants = num_pants * cost_pants

    # Calculate the total cost of everything
    total_cost = total_cost_shirt + total_cost_pants
    result = total_cost
    return result

print(solution())