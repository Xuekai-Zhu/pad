def solution():
    """A man drives 60 mph for 3 hours. How fast would he have to drive over the next 2 hours to get an average speed of 70 mph?"""
    # Define the initial speed and time
    initial_speed = 60
    initial_time = 3

    # Define the total distance covered in the first 3 hours
    initial_distance = initial_speed * initial_time

    # Calculate the distance remaining to cover in the next 2 hours to achieve an average speed of 70 mph
    remaining_distance = ((initial_speed * initial_time) + (70 * 5)) - initial_distance

    # Calculate the speed required to cover the remaining distance in 2 hours
    required_speed = remaining_distance / 2

    # Return the required speed
    result = required_speed
    return result

print(solution())