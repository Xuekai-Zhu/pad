def solution():
    """You walk twice as fast as Mr. Harris, and Mr. Harris took 2 hours to walk to the store. If your destination is 3 times further away than the store Mr. Harris walked to, how many hours will it take you to get there?"""
    # Define Mr. Harris' walking speed and time to walk to the store
    harris_speed = 1
    harris_time = 2

    # Define your walking speed relative to Mr. Harris
    your_speed = 2

    # Define the distance to the store Mr. Harris walked to
    store_distance = 1

    # Calculate the distance to your destination
    destination_distance = store_distance * 3

    # Calculate the time it will take you to walk to your destination
    your_time = destination_distance / your_speed

    # return the result
    result = your_time
    return result

print(solution())