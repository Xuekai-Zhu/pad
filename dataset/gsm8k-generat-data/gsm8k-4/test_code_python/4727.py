def solution():
    """On March 1st the sun sets at 6 PM. Every day after the sun sets 1.2 minutes later. It is 6:10 PM and 40 days after March 1st. How many minutes until the sun sets?"""
    # Define the initial time of sunset and the rate of change
    INITIAL_SUNSET_TIME = 6 * 60  # in minutes
    RATE_OF_CHANGE = 1.2  # in minutes/day

    # Calculate the number of days since March 1st
    days_since_march1st = 40

    # Calculate the total change in time of sunset
    total_change = RATE_OF_CHANGE * days_since_march1st

    # Calculate the current time in minutes since March 1st sunset
    current_time = 6 * 60 + 10

    # Calculate the time until the next sunset in minutes
    time_until_sunset = INITIAL_SUNSET_TIME + total_change - current_time

    result = time_until_sunset
    return result

print(solution())