def solution():
    wood_per_birdhouse = 7
    cost_per_wood = 1.50
    profit_per_birdhouse = 5.50
    birdhouse_cost = wood_per_birdhouse * cost_per_wood + profit_per_birdhouse
    danny_birdhouses = 2
    total_cost = danny_birdhouses * birdhouse_cost
    result = total_cost
    
    return result

print(solution())