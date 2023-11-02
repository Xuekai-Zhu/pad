def solution():
    
    
    total_hours = 1500
    completed_hours = 50 + 9 + 121
    remaining_hours = total_hours - completed_hours
    monthly_hours = 220
    months_needed = remaining_hours / monthly_hours
    result = months_needed
    
    return result

print(solution())