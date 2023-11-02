def solution():
    """The average speed for an hour drive is 66 miles per hour. If Felix wanted to drive twice as fast for 4 hours, how many miles will he cover?"""
    # Define the initial speed and time
    initial_speed = 66
    time = 4

    # Calculate the new speed
    new_speed = initial_speed * 2

    # Calculate the distance covered
    distance = new_speed * time

    result = distance
    return result

print(solution())