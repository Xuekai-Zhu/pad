def solution():
    """A man drives 60 mph for 3 hours.  How fast would he have to drive over the next 2 hours to get an average speed of 70 mph?"""
    # Define the initial velocity and time
    initial_velocity = 60
    initial_time = 3

    # Define the total distance travelled
    total_distance = initial_velocity * initial_time

    # Calculate the required velocity over the next 2 hours to get an average speed of 70 mph
    required_velocity = (total_distance + (70 * 5)) / 5

    # Display the required velocity
    result = required_velocity
    return result

print(solution())