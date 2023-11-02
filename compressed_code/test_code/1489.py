def solution():
    
    planks_cost = 3
    nails_cost = 0.05
    birdhouses = 4
    planks_needed = 7 * birdhouses
    nails_needed = 20 * birdhouses
    total_cost = (planks_cost * planks_needed) + (nails_cost * nails_needed)
    result = total_cost
    return result

print(solution())