def solution():
    loaves_per_hour = 5  # The baker bakes 5 loaves of bread per hour in one oven
    num_ovens = 4  # The baker has 4 ovens
    weekday_hours = 5  # The baker bakes for 5 hours on weekdays
    weekend_hours = 2  # The baker bakes for 2 hours on weekends
    num_weeks = 3  # The baker wants to know how many loaves of bread he bakes in 3 weeks

    # Calculate the total number of hours the baker bakes on weekdays
    total_weekday_hours = weekday_hours * 5  # The baker works for 5 weekdays

    # Calculate the total number of hours the baker bakes on weekends
    total_weekend_hours = weekend_hours * 2  # The baker works for 2 weekends

    # Calculate the total number of loaves of bread the baker bakes in 1 hour
    loaves_per_total_hour = loaves_per_hour * num_ovens

    # Calculate the total number of loaves of bread the baker bakes in 1 day (weekday)
    loaves_per_weekday = loaves_per_total_hour * total_weekday_hours

    # Calculate the total number of loaves of bread the baker bakes in 1 day (weekend)
    loaves_per_weekend = loaves_per_total_hour * total_weekend_hours

    # Calculate the total number of loaves of bread the baker bakes in 3 weeks
    total_loaves = (loaves_per_weekday * 5 + loaves_per_weekend * 2) * num_weeks

    result = total_loaves
    return result

print(solution())