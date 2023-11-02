def solution():
    weekdays = 5  # There are 5 weekdays
    weekend_days = 2  # There are 2 weekend days

    # Calculate the total hours Ralph watches TV on weekdays
    weekday_hours = 4 * weekdays

    # Calculate the total hours Ralph watches TV on weekend days
    weekend_hours = 6 * weekend_days

    # Calculate the total hours spent watching TV in one week
    total_hours = weekday_hours + weekend_hours
    result = total_hours
    return result

print(solution())