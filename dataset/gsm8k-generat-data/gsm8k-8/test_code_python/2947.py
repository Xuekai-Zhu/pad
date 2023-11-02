def solution():
    white_rabbit_speed = 15 # meters/minute
    brown_rabbit_speed = 12 # meters/minute
    time = 5 # minutes

    # Calculate the distance each rabbit would travel
    white_rabbit_distance = white_rabbit_speed * time
    brown_rabbit_distance = brown_rabbit_speed * time

    # Calculate the total distance both rabbits would travel
    total_distance = white_rabbit_distance + brown_rabbit_distance
    result = total_distance
    return result

print(solution())