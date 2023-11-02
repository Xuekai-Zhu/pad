def solution():
    """Samuel took 30 minutes to finish his homework while Sarah took 1.3 hours to finish it. How many minutes faster did Samuel finish his homework than Sarah?"""
    # Define the time taken by Samuel and Sarah in minutes
    samuel_time = 30
    sarah_time = 1.3 * 60

    # Calculate the time difference and convert it to minutes
    time_difference = sarah_time - samuel_time
    time_difference_minutes = time_difference / 60

    # Calculate the time difference in minutes
    result = time_difference_minutes
    return result

print(solution())