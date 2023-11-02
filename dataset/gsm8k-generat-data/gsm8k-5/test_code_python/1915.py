def solution():
    planks_per_birdhouse = 7  # Each birdhouse requires 7 planks
    nails_per_birdhouse = 20  # Each birdhouse requires 20 nails
    cost_per_nail = 0.05  # 1 nail costs $0.05
    cost_per_plank = 3  # 1 plank costs $3
    num_birdhouses = 4  # We want to know the cost to build 4 birdhouses

    # Calculate the total cost of planks for 4 birdhouses
    total_plank_cost = planks_per_birdhouse * cost_per_plank * num_birdhouses

    # Calculate the total cost of nails for 4 birdhouses
    total_nail_cost = nails_per_birdhouse * cost_per_nail * num_birdhouses

    # Calculate the total cost to build 4 birdhouses
    total_cost = total_plank_cost + total_nail_cost
    result = total_cost
    return result

print(solution())