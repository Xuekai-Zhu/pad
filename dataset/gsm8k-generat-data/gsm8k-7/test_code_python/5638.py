def solution():
    weekday_hours = 7
    weekend_hours = 8

    # Calculate the total hours slept during weekdays (5 days per week)
    weekday_total = weekday_hours * 5

    # Calculate the total hours slept during weekends (2 days per week)
    weekend_total = weekend_hours * 2

    # Calculate the total hours slept in a week
    total_hours = weekday_total + weekend_total
    result = total_hours
    return result

print(solution())