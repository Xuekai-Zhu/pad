def solution():
    planks_per_birdhouse = 7
    nails_per_birdhouse = 20
    cost_per_nail = 0.05
    cost_per_plank = 3
    num_birdhouses = 4

    # Calculate the total number of planks needed to build all birdhouses
    total_planks = planks_per_birdhouse * num_birdhouses

    # Calculate the total number of nails needed to build all birdhouses
    total_nails = nails_per_birdhouse * num_birdhouses

    # Calculate the total cost of all planks needed to build all birdhouses
    total_plank_cost = total_planks * cost_per_plank

    # Calculate the total cost of all nails needed to build all birdhouses
    total_nail_cost = total_nails * cost_per_nail

    # Calculate the total cost to build all birdhouses
    total_cost = total_plank_cost + total_nail_cost
    result = total_cost
    return result

print(solution())