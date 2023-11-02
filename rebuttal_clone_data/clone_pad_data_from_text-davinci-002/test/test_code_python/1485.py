def solution():
    hours_per_dress = 12
    dresses_needed = 5
    hours_sewn_per_week = 4
    total_hours = hours_per_dress * dresses_needed
    total_weeks = total_hours / hours_sewn_per_week
    result = total_weeks
    
    return result

print(solution())