def solution():
    """Max can mow the lawn in 40 minutes. If it takes him twice that long to fertilize the lawn, how long will it take him to both mow and fertilize the lawn?"""
    # Define the time it takes for Max to mow the lawn and to fertilize the lawn
    MOW_TIME = 40
    FERTILIZE_TIME = 2 * MOW_TIME

    # Calculate the total time it takes for Max to mow and fertilize the lawn
    total_time = MOW_TIME + FERTILIZE_TIME

    # Display the total time
    result = total_time
    return result

print(solution())