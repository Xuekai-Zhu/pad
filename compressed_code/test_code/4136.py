def solution():
    
    checkered_cost = 75
    plain_cost = 45
    cost_per_yard = 7.5
    total_checkered_yards = checkered_cost / cost_per_yard
    total_plain_yards = plain_cost / cost_per_yard
    total_yards = total_checkered_yards + total_plain_yards
    result = total_yards
    return result

print(solution())