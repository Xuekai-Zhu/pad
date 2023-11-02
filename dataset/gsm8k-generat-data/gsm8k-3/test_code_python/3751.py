def solution():
    """A monkey swings from branch to branch at an average distance of 1.2 meters per second. How far will a monkey swing in meters if it consistently swings from branches for 30 minutes?"""
    # Define the average distance per second the monkey swings
    DISTANCE_PER_SECOND = 1.2

    # Define the number of seconds in 30 minutes
    SECONDS_IN_THIRTY_MINUTES = 1800

    # Calculate the total distance the monkey swings in 30 minutes
    total_distance = DISTANCE_PER_SECOND * SECONDS_IN_THIRTY_MINUTES

    # Display the total distance swung by the monkey
    result = total_distance
    return result

print(solution())