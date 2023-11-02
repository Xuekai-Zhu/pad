def solution():
    """A highway is being extended from its current length of 200 miles up to 650 miles. 50 miles are built on the first day, and three times this amount are built on the second day.  How many miles still need to be added to the highway to finish extending it?"""
    # Calculate the total distance currently left to extend the highway
    total_distance_left = 650 - 200

    # Calculate the distance built on the second day
    distance_built_day2 = 50 * 3

    # Calculate the total distance built so far
    total_distance_built = 50 + distance_built_day2

    # Calculate the distance still needing to be built
    distance_left_to_build = total_distance_left - total_distance_built

    # Display the distance still needing to be built
    result = distance_left_to_build
    return result

print(solution())