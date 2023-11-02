def solution():
    # Calculate the hours of operation on weekdays
    weekday_hours = (10 - 4) * 5

    # Calculate the hours of operation on weekends
    weekend_hours = (10 - 6) * 2

    # Calculate the total hours of operation in a week
    total_hours = weekday_hours + weekend_hours
    result = total_hours
    return result

print(solution())