def solution():
    white_rabbit_speed = 15  # White rabbit can hop 15 meters in one minute
    brown_rabbit_speed = 12  # Brown rabbit can hop 12 meters in one minute
    time = 5  # The rabbits will hop for 5 minutes

    # Calculate the total distance the white rabbit will hop in 5 minutes
    white_rabbit_distance = white_rabbit_speed * time

    # Calculate the total distance the brown rabbit will hop in 5 minutes
    brown_rabbit_distance = brown_rabbit_speed * time

    # Calculate the total distance the two rabbits will hop in 5 minutes
    total_distance = white_rabbit_distance + brown_rabbit_distance
    result = total_distance
    return result

print(solution())