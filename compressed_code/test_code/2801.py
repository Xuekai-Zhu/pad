def solution():
    
    turkey1_weight = 6
    turkey2_weight = 9
    turkey3_weight = 2 * turkey2_weight
    turkey_total_weight = turkey1_weight + turkey2_weight + turkey3_weight
    cost_per_kilogram = 2
    total_cost = turkey_total_weight * cost_per_kilogram
    result = total_cost
    return result

print(solution())