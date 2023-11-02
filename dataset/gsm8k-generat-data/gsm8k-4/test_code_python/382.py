def solution():
    """It takes David 10 minutes to wash 4 windows. David's house has 64 windows. How many minutes will it take David to wash all of the windows?"""
    # Define the time it takes to wash 1 window and the total number of windows
    time_per_window = 10 / 4
    total_windows = 64

    # Calculate the total time to wash all the windows
    total_time = time_per_window * total_windows

    # Return the result
    result = total_time
    return result

print(solution())