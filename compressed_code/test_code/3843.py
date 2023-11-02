def solution():
    
    skirt_area = 12 * 4
    bodice_area = 2 + (5 * 2) 
    total_area = (skirt_area * 3) + bodice_area
    cost_per_square_foot = 3
    total_cost = total_area * cost_per_square_foot
    result = total_cost
    return result

print(solution())