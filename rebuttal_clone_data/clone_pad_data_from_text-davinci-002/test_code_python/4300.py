def solution():
    extra_hours_needed = 5
    normal_hours = 10
    total_hours_needed = 1500
    total_hours = total_hours_needed + (extra_hours_needed * total_hours_needed / normal_hours)
    days_needed = total_hours / (extra_hours_needed + normal_hours)
    result = days_needed
    
    return result

print(solution())