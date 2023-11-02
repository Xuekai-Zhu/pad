def solution():
    """Barry stands on his head for 10 minutes at a time, but then he must sit for 5 minutes before he can take another turn standing on his head. How many turns can Barry take standing on his head during a single 2-hour period?"""
    # Define the time for each cycle
    cycle_time = 10 + 5

    # Calculate the number of cycles in a 2-hour period
    total_time = 120
    cycles = total_time // cycle_time

    # return the result
    result = cycles
    return result

print(solution())