def solution():
    weekday_minutes = 30
    weekend_hours = 2
    num_weeks = 52

    # Calculate the total number of minutes Flynn watches on weekdays in one week
    weekday_total_minutes = 5 * weekday_minutes

    # Calculate the total number of minutes Flynn watches on weekends in one week
    weekend_total_minutes = 2 * weekend_hours * 60

    # Calculate the total number of minutes Flynn watches in one week
    weekly_total_minutes = weekday_total_minutes + weekend_total_minutes

    # Calculate the total number of hours Flynn watches in one week
    weekly_total_hours = weekly_total_minutes / 60

    # Calculate the total number of hours Flynn watches in 52 weeks
    total_hours = weekly_total_hours * num_weeks
    result = total_hours
    return result

print(solution())