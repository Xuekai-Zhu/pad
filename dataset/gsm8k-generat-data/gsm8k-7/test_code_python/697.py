def solution():
    week_days = 5
    weekend_days = 2
    hours_per_night = 2
    weekend_hours_per_day = 3
    weeks_to_exam = 6

    # Calculate the total number of hours Joey spends studying on weekdays
    total_weekday_hours = week_days * hours_per_night * weeks_to_exam

    # Calculate the total number of hours Joey spends studying on weekends
    total_weekend_hours = weekend_days * weekend_hours_per_day * weeks_to_exam

    # Calculate the total number of hours Joey spends studying
    total_hours = total_weekday_hours + total_weekend_hours
    result = total_hours
    return result

print(solution())