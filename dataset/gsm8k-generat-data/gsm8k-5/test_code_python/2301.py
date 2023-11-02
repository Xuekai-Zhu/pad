def solution():
    initial_snowflakes = 10  # There were 10 snowflakes at first
    additional_snowflakes = 4  # It snowed an additional 4 snowflakes every 5 minutes
    target_snowflakes = 58  # The goal is to have 58 snowflakes
    minutes = 0

    while initial_snowflakes < target_snowflakes:
        initial_snowflakes += additional_snowflakes
        minutes += 5

    result = minutes
    return result

print(solution())