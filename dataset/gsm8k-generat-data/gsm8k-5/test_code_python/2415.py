def solution():
    snowflakes_per_5_min = 4  # Additional snowflakes that fall every 5 minutes
    total_time = 60  # Time in minutes
    total_snowflakes = 58  # Total number of snowflakes after 1 hour

    # Calculate the number of snowflakes that fell in the first "x" minutes
    x = 0
    while True:
        if x == 0:
            snowflakes = 0  # No additional snowflakes have fallen
        else:
            snowflakes = ((x // 5) + 1) * snowflakes_per_5_min  # Additional snowflakes have fallen every 5 minutes
        total_snowflakes_x_minutes = snowflakes + snowflakes_per_5_min  # Total number of snowflakes after x minutes
        if total_snowflakes_x_minutes >= total_snowflakes:  # If the total number of snowflakes exceeds the expected value
            break
        x += 1

    # Calculate the number of snowflakes that were there at first
    snowflakes_at_first = total_snowflakes_x_minutes - snowflakes_per_5_min * (x // 5 + 1)
    result = snowflakes_at_first
    return result

print(solution())