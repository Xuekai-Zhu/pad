def solution():
    lexie_speed = 1/20  # miles per minute
    celia_speed = lexie_speed * 2

    distance = 30  # miles

    # Calculate the time it will take Celia to run the distance
    time = distance / celia_speed * 60  # convert to minutes
    result = time
    return result

print(solution())