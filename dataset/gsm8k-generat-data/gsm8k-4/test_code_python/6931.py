def solution():
    """Max can mow the lawn in 40 minutes. If it takes him twice that long to fertilize the lawn, how long will it take him to both mow and fertilize the lawn?"""
    # Define the time it takes to mow the lawn
    mow_time = 40

    # Define the time it takes to fertilize the lawn
    fertilize_time = 2 * mow_time

    # Calculate the total time to do both tasks
    total_time = mow_time + fertilize_time

    # Return the result
    result = total_time
    return result

print(solution())