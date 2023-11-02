def solution():
    """Marcos has to get across a 5 mile lake in his speedboat in 10 minutes so he can make it to work on time. How fast does he need to go in miles per hour to make it?"""
    # Convert time to hours
    time = 10 / 60

    # Calculate the required speed
    speed = 5 / time

    # Convert speed to miles per hour
    mph = speed * 60

    # Display the required speed in miles per hour
    result = mph
    return result

print(solution())