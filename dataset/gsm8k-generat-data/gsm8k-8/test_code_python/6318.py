def solution():
    # Define Lexie's speed and distance
    lexie_speed = 1/20  # 1 mile in 20 minutes
    distance = 30

    # Calculate Celia's speed
    celia_speed = 2 * lexie_speed

    # Calculate the time it will take Celia to run 30 miles
    time = distance / celia_speed * 60  # convert to minutes
    result = time
    return result

print(solution())