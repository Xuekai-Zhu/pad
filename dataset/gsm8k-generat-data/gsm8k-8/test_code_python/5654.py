def solution():
    # Calculate the number of minutes practiced during the weekdays
    weekday_minutes = 15 * 5

    # Calculate the number of minutes practiced each weekend day
    weekend_minutes = 15 * 2 * 2

    # Calculate the total number of minutes practiced in a week
    total_minutes = weekday_minutes + weekend_minutes
    result = total_minutes
    return result

print(solution())