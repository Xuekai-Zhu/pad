def solution():
    
    pasta_cost = 1
    cheddar_cost = 3
    gruyere_cost = 2 * cheddar_cost
    total_cost = (pasta_cost + cheddar_cost + gruyere_cost) * 52
    result = total_cost
    return result

print(solution())