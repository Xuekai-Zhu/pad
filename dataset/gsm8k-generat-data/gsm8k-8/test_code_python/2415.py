def solution():
    # Number of snowflakes added per 5-minute interval
    snowflakes_per_interval = 4
    
    # Number of 5-minute intervals in an hour
    intervals_in_hour = 60 / 5
    
    # Total number of snowflakes after 1 hour
    total_snowflakes = 58
    
    # Calculate the number of snowflakes at first
    initial_snowflakes = total_snowflakes - snowflakes_per_interval * (intervals_in_hour - 1)
    result = initial_snowflakes
    return result

print(solution())