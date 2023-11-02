def solution():
    # Calculate Mr. Harris' walking speed and time
    harris_speed = 1/2  # in miles per hour
    harris_time = 2  # in hours

    # Calculate your walking speed
    your_speed = 2 * harris_speed

    # Calculate the distance to your destination
    store_distance = 1  # assumed to be 1 mile
    destination_distance = 3 * store_distance

    # Calculate the time it will take you to get to your destination
    destination_time = destination_distance / your_speed
    result = destination_time
    return result

print(solution())