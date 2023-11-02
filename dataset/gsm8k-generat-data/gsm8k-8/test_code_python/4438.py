def solution():
    # Calculate the total number of weekdays in the semester
    weekdays = 5 * 15

    # Calculate the total number of hours Paris studies during weekdays
    weekday_hours = 3 * weekdays

    # Calculate the total number of hours Paris studies on the weekends
    weekend_hours = 4 + 5

    # Calculate the total number of weekends in the semester
    weekends = 15 // 7

    # Calculate the total number of hours Paris studies on the weekends during the semester
    weekend_total_hours = weekend_hours * weekends

    # Calculate the total number of hours Paris studies during the semester
    total_hours = weekday_hours + weekend_total_hours

    result = total_hours
    return result

print(solution())