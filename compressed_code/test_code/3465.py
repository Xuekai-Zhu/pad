def solution():
    
    weekday_hours = (10 - 4)  
    weekend_hours = (10 - 6)  
    total_weekday_hours = weekday_hours * 5  
    total_weekend_hours = weekend_hours * 2  
    total_hours = total_weekday_hours + total_weekend_hours
    result = total_hours
    return result

print(solution())