def solution():
    # Calculate the total number of hours Ludwig works during Friday, Saturday, and Sunday
    half_day_hours = 4 # assuming a half day is 4 hours
    weekend_hours = half_day_hours * 3

    # Calculate the total number of hours Ludwig works during the rest of the week
    weekday_hours = 10 * 4 # assuming Ludwig works 10 hours on weekdays

    # Calculate the total number of hours Ludwig works per week
    total_hours = weekday_hours + weekend_hours

    # Calculate Ludwig's weekly salary
    salary_per_hour = 10
    weekly_salary = total_hours * salary_per_hour
    result = weekly_salary
    return result

print(solution())