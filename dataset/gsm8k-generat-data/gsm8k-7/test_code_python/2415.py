def solution():
    snowflakes_per_5min = 4
    time_in_hours = 1
    total_time_in_minutes = time_in_hours * 60
    total_snowflakes = 58

    # Calculate the additional snowflakes for the entire hour
    additional_snowflakes = snowflakes_per_5min * (total_time_in_minutes // 5)

    # Calculate the initial number of snowflakes
    initial_snowflakes = total_snowflakes - additional_snowflakes

    result = initial_snowflakes
    return result

print(solution())