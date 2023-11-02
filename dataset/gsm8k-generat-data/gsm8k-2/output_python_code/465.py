def solution():
    """At Snowflake Plastics, each employee gets 10 sick days and 10 vacation days per year. If Mark uses half his allotment of both types of days in a year, how many hours' worth of days does he have left if each day covers an 8-hour long workday?"""
    
    # Calculate total number of sick and vacation days Mark has
    total_days = 10 + 10
    
    # Calculate how many days Mark has used up
    used_days = total_days / 2
    
    # Calculate how many hours Mark has left based on the remaining days
    remaining_days = total_days - used_days
    hours_left = remaining_days * 8
    
    result = hours_left
    return result

print(solution())