def solution():
    # Calculate the total hours of operation on weekdays
    weekday_hours = (10 - 4) * 5  # Open from 4 pm to 10 pm, 5 days a week

    # Calculate the total hours of operation on weekends
    weekend_hours = (10 - 6) * 2  # Open from 6 pm to 10 pm, 2 days a week

    # Calculate the total hours of operation in a week
    total_hours = weekday_hours + weekend_hours
    result = total_hours
    return result

print(solution())