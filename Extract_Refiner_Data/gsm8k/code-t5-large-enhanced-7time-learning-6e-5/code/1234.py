def solution():
    
    pasta_cost = 1.00
    cheddar_cheese_cost = 3.00
    gruyere_cheese_cost = 2 * cheddar_cheese_cost
    total_cost = (pasta_cost + cheddar_cheese_cost + gruyere_cheese_cost) * 7
    result = total_cost
    return result

print(solution())