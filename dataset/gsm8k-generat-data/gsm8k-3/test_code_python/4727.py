def solution():
    """
    On March 1st the sun sets at 6 PM. Every day after the sun sets 1.2 minutes later. It is 6:10 PM and 40 days after March 1st. How many minutes until the sun sets?
    """
    # Calculate the number of minutes the sun sets later every day
    daily_increase = 1.2

    # Calculate the number of days since March 1st
    days_since_march_1st = 40

    # Calculate the total number of minutes the sun sets later than 6 PM on March 1st
    total_increase = daily_increase * days_since_march_1st

    # Calculate the current time in minutes since 6 PM
    current_time = 10

    # Calculate the number of minutes until the sun sets
    minutes_until_sunset = 60 - (current_time + total_increase)

    # Display the number of minutes until the sun sets
    result = minutes_until_sunset
    return result

print(solution())