def solution():
    # Calculate the total number of weekdays in 3 weeks
    weekdays_in_3_weeks = 15

    # Calculate the total number of hours Mike will practice on weekdays
    weekday_hours = 3 * weekdays_in_3_weeks

    # Calculate the total number of hours Mike will practice on Saturdays
    saturday_hours = 5 * 3

    # Calculate the total number of hours Mike will practice for the next game
    total_hours = weekday_hours + saturday_hours

    result = total_hours
    return result

print(solution())