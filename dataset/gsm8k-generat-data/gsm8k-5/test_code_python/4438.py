def solution():
    weekdays_per_week = 5  # Paris studies 3 hours per day on weekdays
    weekend_hours = 4 + 5  # Paris studies 4 hours on Saturday and 5 hours on Sunday
    total_days = 15 * 7  # There are 15 weeks in a semester, with 7 days per week

    # Calculate the total number of hours Paris studies on weekdays
    weekday_hours = weekdays_per_week * total_days * 3

    # Calculate the total number of hours Paris studies on weekends
    weekend_days = total_days - (15 * 5)  # Subtract the weekdays from the total days
    weekend_total = weekend_days * weekend_hours

    # Calculate the total number of hours Paris studies during the semester
    total_hours = weekday_hours + weekend_total
    result = total_hours
    return result

print(solution())