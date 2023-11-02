def solution():
    """A pipe is clogged so that only 2 ounces of cleaner can run through the pipe per minute. After fifteen minutes, the cleaner has unclogged it enough that 3 ounces can run through per minute. Ten minutes later, the clog is cleared enough for 4 ounces to run through per minute. How many ounces of cleaner were used after 30 minutes?"""
    # Define the flow rates and time intervals
    flow_rate_1 = 2
    flow_rate_2 = 3
    flow_rate_3 = 4
    time_interval_1 = 15
    time_interval_2 = 10
    time_interval_3 = 5

    # Calculate the total amount of cleaner used during each time interval
    cleaner_used_1 = flow_rate_1 * time_interval_1
    cleaner_used_2 = (flow_rate_2 - flow_rate_1) * time_interval_2
    cleaner_used_3 = (flow_rate_3 - flow_rate_2) * time_interval_3

    # Calculate the total amount of cleaner used in 30 minutes
    total_cleaner_used = cleaner_used_1 + cleaner_used_2 + cleaner_used_3

    # Return the result
    result = total_cleaner_used
    return result

print(solution())