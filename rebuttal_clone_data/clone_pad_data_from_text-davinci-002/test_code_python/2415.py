def solution():
    snowflakes = 58
    time_interval = 5
    time = 1
    num_of_intervals = time / time_interval
    additional_snowflakes = num_of_intervals * 4
    initial_snowflakes = snowflakes - additional_snowflakes
    result = initial_snowflakes
    return result

print(solution())