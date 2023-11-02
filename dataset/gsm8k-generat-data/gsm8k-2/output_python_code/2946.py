def solution():
    """The white rabbit can hop 15 meters in one minute. The brown rabbit hops 12 meters per minute. What is the total distance the two rabbits will hop in 5 minutes?"""
    white_rabbit_speed = 15
    brown_rabbit_speed = 12
    time = 5
    total_distance = (white_rabbit_speed + brown_rabbit_speed) * time
    result = total_distance
    return result

print(solution())