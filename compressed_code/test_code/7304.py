def solution():
    
    planks_per_birdhouse = 7
    nails_per_birdhouse = 20
    cost_per_nail = 0.05
    cost_per_plank = 3.0
    birdhouses_to_build = 4
    
    total_planks = planks_per_birdhouse * birdhouses_to_build
    total_nails = nails_per_birdhouse * birdhouses_to_build
    total_plank_cost = cost_per_plank * total_planks
    total_nail_cost = cost_per_nail * total_nails
    total_cost = total_plank_cost + total_nail_cost
    
    result = total_cost
    return result

print(solution())