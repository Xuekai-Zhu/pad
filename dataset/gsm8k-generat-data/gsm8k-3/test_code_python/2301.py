def solution():
    """There were 10 snowflakes at first. It snowed an additional 4 snowflakes every 5 minutes. How many minutes passed before there were 58 snowflakes?"""
    # Define the initial number of snowflakes and the additional snowflakes per 5 minutes
    initial_snowflakes = 10
    additional_snowflakes = 4

    # Define the target number of snowflakes
    target_snowflakes = 58

    # Compute the number of snowflakes added in each time interval
    added_snowflakes = additional_snowflakes * 5

    # Compute the number of time intervals required to reach the target snowflake count
    time_intervals = (target_snowflakes - initial_snowflakes) // added_snowflakes

    # Compute the total time in minutes
    total_time = time_intervals * 5

    # Display the total time in minutes
    result = total_time
    return result

print(solution())