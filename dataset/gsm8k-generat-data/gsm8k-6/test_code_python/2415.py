def solution():
    # Calculate the number of snowflakes that fell in the first hour
    additional_snowflakes_per_hour = 4 * 12  # 4 snowflakes every 5 minutes for 12 sets of 5 minutes in an hour
    total_snowflakes = 58  # total number of snowflakes after 1 hour
    initial_snowflakes = total_snowflakes - additional_snowflakes_per_hour  # calculate the number of snowflakes at first
    result = initial_snowflakes
    return result

print(solution())