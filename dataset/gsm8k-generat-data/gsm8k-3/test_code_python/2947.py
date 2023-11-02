def solution():
    """The white rabbit can hop 15 meters in one minute. The brown rabbit hops 12 meters per minute. What is the total distance the two rabbits will hop in 5 minutes?"""
    # Define the hopping rates of the rabbits
    white_rate = 15  # meters per minute
    brown_rate = 12  # meters per minute

    # Calculate the total distance each rabbit will hop in 5 minutes
    white_distance = white_rate * 5
    brown_distance = brown_rate * 5

    # Calculate the total distance both rabbits will hop in 5 minutes
    total_distance = white_distance + brown_distance

    # Display the total distance
    result = total_distance
    return result

print(solution())