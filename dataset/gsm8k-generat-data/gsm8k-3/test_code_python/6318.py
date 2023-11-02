def solution():
    """Celia runs twice as fast as Lexie. If it takes Lexie 20 minutes to run a mile, how long, in minutes, will it take Celia to 30 miles?"""
    # Calculate Lexie's speed in miles per minute
    lexie_speed = 1/20 # 1 mile in 20 minutes

    # Calculate Celia's speed in miles per minute
    celia_speed = 2 * lexie_speed # twice as fast as Lexie

    # Calculate the time it will take Celia to run 30 miles
    time = 30 / celia_speed

    # Convert the time to minutes and round to the nearest minute
    minutes = round(time * 60)

    # Display the time in minutes
    result = minutes
    return result

print(solution())