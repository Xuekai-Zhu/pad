def solution():
    
    total_hours = 5
    monday_wednesday_hours = 1.5 * 2
    tuesday_friday_hours = (total_hours - monday_wednesday_hours) / 2
    friday_hours = tuesday_friday_hours
    result = friday_hours
    return result

print(solution())