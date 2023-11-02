def solution():
    
    tuesday_hours = 1
    thursday_hours = 2
    saturday_hours = tuesday_hours * 2
    total_hours = tuesday_hours + thursday_hours + saturday_hours
    weekly_hours = total_hours * 7
    result = weekly_hours
    return result

print(solution())