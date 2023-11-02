def solution():
    """At Snowflake Plastics, each employee gets 10 sick days and 10 vacation days per year. If Mark uses half his allotment of both types of days in a year, how many hours' worth of days does he have left if each day covers an 8-hour long workday?"""
    # Define the number of sick days and vacation days each employee gets
    SICK_DAYS = 10
    VACATION_DAYS = 10

    # Calculate the number of sick days and vacation days Mark has used
    sick_days_used = SICK_DAYS / 2
    vacation_days_used = VACATION_DAYS / 2

    # Calculate the number of hours of sick and vacation time Mark has left
    sick_hours_left = (SICK_DAYS - sick_days_used) * 8
    vacation_hours_left = (VACATION_DAYS - vacation_days_used) * 8

    # Calculate the total number of hours of sick and vacation time Mark has left
    total_hours_left = sick_hours_left + vacation_hours_left

    # Return the result
    result = total_hours_left
    return result

print(solution())