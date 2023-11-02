def solution():
    # Find Celia's running speed in miles per minute (since Lexie runs 1 mile in 20 minutes)
    lexie_speed = 1/20
    celia_speed = 2 * lexie_speed

    # Calculate the time it will take for Celia to run 30 miles (d = rt)
    distance = 30
    time = distance / celia_speed
    result = time * 60  # convert to minutes
    return result

print(solution())