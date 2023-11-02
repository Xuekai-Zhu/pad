def solution():
    """There were some snowflakes at first. It snowed an additional 4 snowflakes every 5 minutes. If there were 58 snowflakes after 1 hour, how many snowflakes were there at first?"""
    # Define the number of snowflakes added every 5 minutes
    SNOWFLAKES_PER_INTERVAL = 4

    # Define the number of intervals in an hour
    INTERVALS_PER_HOUR = 12

    # Define the total number of snowflakes after 1 hour
    total_snowflakes = 58

    # Calculate the number of snowflakes added in 1 hour
    snowflakes_added = SNOWFLAKES_PER_INTERVAL * INTERVALS_PER_HOUR

    # Calculate the number of snowflakes at first
    snowflakes_at_first = total_snowflakes - snowflakes_added

    # return the result
    result = snowflakes_at_first
    return result

print(solution())