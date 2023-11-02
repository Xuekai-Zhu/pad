def solution():
    """There were some snowflakes at first. It snowed an additional 4 snowflakes every 5 minutes. If there were 58 snowflakes after 1 hour, how many snowflakes were there at first?"""
    # Define the number of snowflakes added every 5 minutes
    SNOWFLAKE_ADDITION = 4

    # Convert 1 hour to minutes
    time = 60

    # Define the total number of snowflakes after 1 hour
    total_snowflakes = 58

    # Calculate the number of snowflakes that fell after the initial period
    additional_snowflakes = (time // 5) * SNOWFLAKE_ADDITION

    # Calculate the number of snowflakes at the beginning
    initial_snowflakes = total_snowflakes - additional_snowflakes

    # Display the number of snowflakes at the beginning
    result = initial_snowflakes
    return result

print(solution())