def solution():
    cost_per_nail = 0.05
    cost_per_plank = 3
    planks_required = 7
    nails_required = 20
    
    # Calculate the total cost to build 1 birdhouse
    total_cost = (cost_per_nail * nails_required) + (cost_per_plank * planks_required)
    
    # Calculate the total cost to build 4 birdhouses
    total_cost_4_birdhouses = total_cost * 4
    result = total_cost_4_birdhouses
    return result

print(solution())