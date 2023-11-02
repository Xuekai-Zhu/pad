def solution():
    # Calculate the hours spent catching up on the weekend
    weekend_catching_up_hours = 3 * weekend_working_hours

    # Calculate the hours spent working on the weekdays
    weekday_working_hours = 4 * weekday_catching_up_hours

    # Calculate the total hours worked in a week
    total_hours_worked = weekday_working_hours * 5 + weekend_working_hours * 2
    result = total_hours_worked
    return result

print(solution())