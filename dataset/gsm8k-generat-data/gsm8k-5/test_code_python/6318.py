def solution():
    # Calculate Lexie's speed in miles per minute
    lexie_speed = 1 / (20 / 60)  # 20 minutes to run 1 mile

    # Calculate Celia's speed in miles per minute
    celia_speed = lexie_speed * 2  # Celia runs twice as fast as Lexie

    # Calculate the time it will take Celia to run 30 miles
    time_celia = 30 / celia_speed  # Distance / speed = time
    result = time_celia
    return result

print(solution())