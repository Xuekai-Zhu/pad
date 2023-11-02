def solution():
    
    length = 30
    width = 40
    area = length * width
    cost_per_sqft = 3
    sealant_cost_per_sqft = 1
    total_cost = (area * cost_per_sqft) + (area * sealant_cost_per_sqft)
    result = total_cost
    return result

print(solution())