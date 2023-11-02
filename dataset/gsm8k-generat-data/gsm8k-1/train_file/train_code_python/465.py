def solution():
    """At Snowflake Plastics, each employee gets 10 sick days and 10 vacation days per year. If Mark uses half his allotment of both types of days in a year, how many hours' worth of days does he have left if each day covers an 8-hour long workday?"""
    sick_days_allotted = 10
    vacation_days_allotted = 10
    days_used = (sick_days_allotted + vacation_days_allotted) / 2
    hours_left = (sick_days_allotted + vacation_days_allotted - days_used) * 8
    result = hours_left
    return result

print(solution())