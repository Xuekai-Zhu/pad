def solution():
    
    total_hours = 1500
    completed_hours = 50 + 9 + 121
    remaining_hours = total_hours - completed_hours
    months = 6
    hours_per_month = remaining_hours / months
    result = hours_per_month
    return result

print(solution())