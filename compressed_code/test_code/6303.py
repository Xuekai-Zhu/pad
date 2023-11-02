def solution():
    
    total_roofing_needed = 300
    cost_per_foot = 8
    free_roofing = 250
    remaining_roofing_needed = total_roofing_needed - free_roofing
    total_cost = remaining_roofing_needed * cost_per_foot
    result = total_cost
    
    return result

print(solution())