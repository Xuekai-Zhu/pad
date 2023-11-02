def solution():
    """Every day Janet spends 8 minutes looking for her keys and another 3 minutes complaining after she finds them. If Janet stops losing her keys, how many minutes will she save every week?"""
    # Define the time Janet spends looking for her keys and complaining each day
    LOOKING_TIME = 8
    COMPLAINING_TIME = 3

    # Calculate the total time Janet spends looking for her keys and complaining each day
    total_time = LOOKING_TIME + COMPLAINING_TIME

    # Calculate the amount of time Janet will save every week if she stops losing her keys
    minutes_saved_per_week = total_time * 7

    # Display the amount of time Janet will save every week
    result = minutes_saved_per_week
    return result

print(solution())