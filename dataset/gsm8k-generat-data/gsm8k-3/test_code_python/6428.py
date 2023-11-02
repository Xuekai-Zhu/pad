def solution():
    """Percy swims 1 hour before school and 1 after school 5 days a week.  He swims 3 hours on the weekend.  How many hours of swimming does he do over 4 weeks?"""
    # Define the number of hours Percy swims per day during the week
    WEEKDAY_HOURS = 2

    # Define the number of hours Percy swims on the weekend
    WEEKEND_HOURS = 3

    # Calculate the total number of hours Percy swims per week
    weekly_hours = WEEKDAY_HOURS * 5 + WEEKEND_HOURS

    # Calculate the total number of hours Percy swims over 4 weeks
    total_hours = weekly_hours * 4

    # Display the total number of hours
    result = total_hours
    return result

print(solution())