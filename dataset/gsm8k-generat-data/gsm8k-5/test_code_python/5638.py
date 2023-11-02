def solution():
    weekdays = 5  # Janna sleeps 7 hours each weekday
    weekend_days = 2  # Janna sleeps 8 hours each weekend day
    weekday_hours = 7
    weekend_hours = 8

    # Calculate total hours slept in a week
    total_hours = (weekday_hours * weekdays) + (weekend_hours * weekend_days)
    result = total_hours
    return result

print(solution())