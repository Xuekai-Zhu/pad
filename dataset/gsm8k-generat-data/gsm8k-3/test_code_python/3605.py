def solution():
    """You walk twice as fast as Mr. Harris, and Mr. Harris took 2 hours to walk to the store. If your destination is 3 times further away than the store Mr. Harris walked to, how many hours will it take you to get there?"""
    # Get the distance Mr. Harris walked
    distance_harris = 1

    # Calculate your walking speed relative to Mr. Harris
    speed_ratio = 2

    # Calculate the distance to your destination
    distance_yours = 3 * distance_harris

    # Calculate your walking time
    time_yours = distance_yours / (speed_ratio * 1)

    # Display the time it will take you to get to your destination
    result = time_yours
    return result

print(solution())