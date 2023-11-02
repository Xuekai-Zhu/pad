def solution():
    """Barry stands on his head for 10 minutes at a time, but then he must sit for 5 minutes before he can take another turn standing on his head.  How many turns can Barry take standing on his head during a single 2-hour period?"""
    # Convert 2 hours to minutes
    time_period = 2 * 60

    # Calculate the time it takes for each turn (standing + sitting)
    turn_time = 10 + 5

    # Calculate the number of turns Barry can take in the time period
    turns = time_period // turn_time

    # Display the number of turns
    result = turns
    return result

print(solution())