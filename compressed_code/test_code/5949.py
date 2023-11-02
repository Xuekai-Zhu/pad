def solution():
    
    total_weeks = (20 - 12) * 52 
    total_days = total_weeks * 5 
    total_vacation_weeks = 2 * 8 
    total_practice_days = total_days - total_vacation_weeks * 5 
    hours_per_day = 10000 / total_practice_days 
    result = hours_per_day
    return result

print(solution())