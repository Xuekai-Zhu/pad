def solution():
    """The white rabbit can hop 15 meters in one minute. The brown rabbit hops 12 meters per minute. What is the total distance the two rabbits will hop in 5 minutes?"""
    # Define the hopping speeds of the rabbits
    white_speed = 15
    brown_speed = 12

    # Calculate the total distance hopped by the two rabbits in 5 minutes
    total_distance = (white_speed + brown_speed) * 5

    # return the result
    result = total_distance
    return result

print(solution())