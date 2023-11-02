def solution():
    """The white rabbit can hop 15 meters in one minute. The brown rabbit hops 12 meters per minute. What is the total distance the two rabbits will hop in 5 minutes?"""
    white_rabbit_speed = 15
    brown_rabbit_speed = 12
    time = 5
    distance_covered_by_white_rabbit = white_rabbit_speed * time
    distance_covered_by_brown_rabbit = brown_rabbit_speed * time
    total_distance = distance_covered_by_white_rabbit + distance_covered_by_brown_rabbit
    result = total_distance
    return result

print(solution())