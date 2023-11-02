def solution():
    hours_weekday = 4
    hours_weekend = 6

    # Calculate the total hours spent on weekdays
    total_weekday_hours = hours_weekday * 5

    # Calculate the total hours spent on weekends
    total_weekend_hours = hours_weekend * 2

    # Calculate the total hours spent in one week
    total_hours = total_weekday_hours + total_weekend_hours
    result = total_hours
    return result

print(solution())