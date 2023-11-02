def solution():
    """There were 10 snowflakes at first. It snowed an additional 4 snowflakes every 5 minutes. How many minutes passed before there were 58 snowflakes?"""
    # Define the initial number of snowflakes and the rate of increase
    initial_snowflakes = 10
    rate_of_increase = 4
    time_elapsed = 0

    # Keep adding snowflakes every 5 minutes until there are 58 snowflakes
    while initial_snowflakes < 58:
        initial_snowflakes += rate_of_increase
        time_elapsed += 5

    # Display the total time elapsed in minutes
    result = time_elapsed
    return result

print(solution())