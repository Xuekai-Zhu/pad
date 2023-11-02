def solution():
    weekdays = 5  # Number of weekdays in a week
    weekend_days = 2  # Saturday and Sunday
    weekday_hours = 3  # Hours practiced on weekdays
    weekend_hours = 5  # Hours practiced on weekends
    weeks = 3  # Time until the next game in weeks

    # Calculate the hours Mike will practice on weekdays
    weekday_total = weekdays * weekday_hours * weeks

    # Calculate the hours Mike will practice on weekends
    weekend_total = weekend_days * weekend_hours * weeks

    # Calculate the total hours he will practice
    total_hours = weekday_total + weekend_total
    result = total_hours
    return result

print(solution())