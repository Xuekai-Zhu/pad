def solution():
    
    monday_hours = 4
    tuesday_hours = monday_hours * 2
    wednesday_hours = thursday_hours = friday_hours = 3
    total_hours = 25
    weekday_hours = monday_hours + tuesday_hours + wednesday_hours + thursday_hours + friday_hours
    weekend_hours = (total_hours - weekday_hours) / 2  
    saturday_hours = weekend_hours
    result = saturday_hours
    return result

print(solution())