def solution():
    initial_snowflakes = 10
    snowflakes_added = 4
    time_elapsed = 0
    total_snowflakes = initial_snowflakes
    while total_snowflakes < 58:
        time_elapsed += 5
        total_snowflakes += snowflakes_added
    result = time_elapsed
    return result

print(solution())