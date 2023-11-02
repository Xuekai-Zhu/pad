def solution():
    """Celia runs twice as fast as Lexie. If it takes Lexie 20 minutes to run a mile, how long, in minutes, will it take Celia to 30 miles?"""
    # Define Lexie's speed and time
    lexie_speed = 1 / 20  # mile per minute
    lexie_time = 30 / lexie_speed

    # Define Celia's speed (twice Lexie's speed)
    celia_speed = 2 * lexie_speed

    # Calculate Celia's time to run 30 miles
    celia_time = 30 / celia_speed

    # return the result
    result = celia_time
    return result

print(solution())