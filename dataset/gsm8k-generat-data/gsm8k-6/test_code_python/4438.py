def solution():
    # Calculate the total number of weekdays and weekends during the semester
    weekdays = 15 * 5  # there are 5 weekdays in a week
    weekends = 15 * 2  # there are 2 weekend days in a week

    # Calculate the total number of hours Paris spends studying
    weekday_hours = weekdays * 3  # she spends 3 hours studying on weekdays
    weekend_hours = weekends * (4 + 5)  # she spends 4 hours on Saturday and 5 hours on Sunday
    total_hours = weekday_hours + weekend_hours

    result = total_hours
    return result

print(solution())