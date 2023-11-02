def solution():
    
    turquoise_cost = 13
    purple_cost = 11
    wall1_area = 5 * 8
    wall2_area = 7 * 8
    total_area = wall1_area + wall2_area
    tiles_needed = total_area * 4
    turquoise_total_cost = turquoise_cost * tiles_needed
    purple_total_cost = purple_cost * tiles_needed
    savings = turquoise_total_cost - purple_total_cost
    result = savings
    
    return result

print(solution())