def solution():
    """There were 10 snowflakes at first. It snowed an additional 4 snowflakes every 5 minutes. How many minutes passed before there were 58 snowflakes?"""
    initial_snowflakes = 10
    additional_snowflakes = 4
    target_snowflakes = 58
    minutes = 0
    while initial_snowflakes < target_snowflakes:
        initial_snowflakes += additional_snowflakes
        minutes += 5
        
    result = minutes
    return result

print(solution())