def solution():
    
    sheets_per_ream = 500
    cost_per_ream = 27
    total_sheets_needed = 5000
    total_reams_needed = total_sheets_needed / sheets_per_ream
    total_cost = total_reams_needed * cost_per_ream
    result = total_cost
    return result

print(solution())