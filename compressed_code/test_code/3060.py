def solution():
    
    total_weekly_hours = 5
    monday_and_wednesday_hours = 1.5 + 1.5
    tuesday_and_friday_hours = (total_weekly_hours - monday_and_wednesday_hours) / 2
    friday_hours = tuesday_and_friday_hours
    result = friday_hours
    return result

print(solution())