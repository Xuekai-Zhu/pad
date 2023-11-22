def solution():
    
    bedroom_area = 18 * 12
    new_carpet_cost = (bedroom_area * 12) + (2 * bedroom_area)
    contractor_cost = 4 * bedroom_area
    installed_cost = 34 * bedroom_area
    total_cost = new_carpet_cost - contractor_cost + installed_cost
    result = total_cost
    return result

print(solution())