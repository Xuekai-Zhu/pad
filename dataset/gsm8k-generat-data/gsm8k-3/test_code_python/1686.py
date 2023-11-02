def solution():
    """Every day, Bob logs 10 hours of work in his office. If he works for five days a week, calculate the total number of hours he logs in a month."""
    # Define the number of workdays in a week and weeks in a month
    WORKDAYS_PER_WEEK = 5
    WEEKS_PER_MONTH = 4

    # Define Bob's daily work hours
    WORK_HOURS_PER_DAY = 10

    # Calculate the total work hours per month
    total_work_hours = WORKDAYS_PER_WEEK * WEEKS_PER_MONTH * WORK_HOURS_PER_DAY

    # Display the total work hours per month
    result = total_work_hours
    return result

print(solution())