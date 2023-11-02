def solution():
    white_rabbit_speed = 15  # meters per minute
    brown_rabbit_speed = 12  # meters per minute
    time = 5  # minutes

    # Calculate the distance the white rabbit hops in 5 minutes
    white_rabbit_distance = white_rabbit_speed * time

    # Calculate the distance the brown rabbit hops in 5 minutes
    brown_rabbit_distance = brown_rabbit_speed * time

    # Calculate the total distance both rabbits will hop in 5 minutes
    total_distance = white_rabbit_distance + brown_rabbit_distance
    result = total_distance
    return result

print(solution())