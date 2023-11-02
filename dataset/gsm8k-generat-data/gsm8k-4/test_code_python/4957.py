def solution():
    """Jan enters a double dutch competition.  After training she doubles her speed which used to be 70 skips per minute.  How many skips does she do in 5 minutes?"""
    # Define the original speed and the time of skipping
    original_speed = 70
    time = 5

    # Calculate the new speed after training
    new_speed = original_speed * 2

    # Calculate the number of skips in 5 minutes at the new speed
    skips = new_speed * time

    # Return the result
    result = skips
    return result

print(solution())