def solution():
    weekdays_hours = 6 # 4pm to 10 pm is 6 hours
    weekends_hours = 4 # 6pm to 10 pm is 4 hours
    total_weekdays = 5 # Monday to Friday
    total_weekends = 2 # Saturday and Sunday
    
    # Calculate total hours on weekdays
    total_weekdays_hours = weekdays_hours * total_weekdays
    
    # Calculate total hours on weekends
    total_weekends_hours = weekends_hours * total_weekends
    
    # Calculate total hours in a week
    total_hours = total_weekdays_hours + total_weekends_hours
    result = total_hours
    return result

print(solution())