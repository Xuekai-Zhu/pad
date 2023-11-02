def solution():
    
    checkered_cost = 75
    plain_cost = 45
    fabric_cost_per_yard = 7.5
    total_cost = checkered_cost + plain_cost
    total_yards = total_cost / fabric_cost_per_yard
    result = total_yards
    return result

print(solution())