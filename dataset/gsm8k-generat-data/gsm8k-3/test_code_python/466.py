def solution():
    """At Snowflake Plastics, each employee gets 10 sick days and 10 vacation days per year.  If Mark uses half his allotment of both types of days in a year, how many hours' worth of days does he have left if each day covers an 8-hour long workday?"""
    # Define the number of sick days and vacation days per year
    SICK_DAYS_PER_YEAR = 10
    VACATION_DAYS_PER_YEAR = 10

    # Define the length of a workday in hours
    WORKDAY_HOURS = 8

    # Calculate the total number of hours Mark has for sick and vacation days
    total_hours = (SICK_DAYS_PER_YEAR + VACATION_DAYS_PER_YEAR) * WORKDAY_HOURS

    # Calculate the number of hours Mark has used up
    hours_used = (SICK_DAYS_PER_YEAR/2 + VACATION_DAYS_PER_YEAR/2) * WORKDAY_HOURS

    # Calculate the number of hours Mark has remaining for sick and vacation days
    hours_remaining = total_hours - hours_used

    # Display the number of hours remaining
    result = hours_remaining
    return result

print(solution())