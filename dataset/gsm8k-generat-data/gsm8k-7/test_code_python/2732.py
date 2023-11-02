def solution():
    loaves_per_hour = 5
    num_ovens = 4
    
    weekdays_hours = 5
    weekend_hours = 2
    
    num_weeks = 3
    
    # Calculate the total hours of baking for each type of day
    total_weekday_hours = weekdays_hours * 5
    total_weekend_hours = weekend_hours * 2
    
    # Calculate the total loaves of bread baked during weekdays
    total_weekday_loaves = loaves_per_hour * num_ovens * total_weekday_hours
    
    # Calculate the total loaves of bread baked during weekends
    total_weekend_loaves = loaves_per_hour * num_ovens * total_weekend_hours
    
    # Calculate the total loaves of bread baked in 3 weeks
    total_loaves = (total_weekday_loaves + total_weekend_loaves) * num_weeks
    result = total_loaves
    return result

print(solution())