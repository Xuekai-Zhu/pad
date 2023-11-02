def solution():
    """Marcos has to get across a 5 mile lake in his speedboat in 10 minutes so he can make it to work on time. How fast does he need to go in miles per hour to make it?"""
    # Define the distance and time
    distance = 5    # in miles
    time = 10/60    # in hours

    # Calculate the required speed in miles per hour
    speed = distance / time

    # Return the result
    result = speed
    return result

print(solution())