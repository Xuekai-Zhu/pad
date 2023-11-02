def solution():
    
    width = 30
    length = 40
    area = width * length
    cost_per_sq_foot = 3
    sealant_cost_per_sq_foot = 1
    total_cost = area * (cost_per_sq_foot + sealant_cost_per_sq_foot)
    result = total_cost
    return result

print(solution())