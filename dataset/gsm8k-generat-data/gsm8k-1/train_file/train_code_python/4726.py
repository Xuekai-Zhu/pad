def solution():
    """On March 1st the sun sets at 6 PM. Every day after the sun sets 1.2 minutes later. It is 6:10 PM and 40 days after March 1st. How many minutes until the sun sets?"""
    sunset_time = 6 * 60  # convert to minutes
    daily_increase = 1.2
    days = 40
    total_increase = daily_increase * days
    current_time = 6 * 60 + 10  # add 10 minutes for 6:10 PM
    minutes_until_sunset = sunset_time + total_increase - current_time
    result = minutes_until_sunset
    return result

print(solution())