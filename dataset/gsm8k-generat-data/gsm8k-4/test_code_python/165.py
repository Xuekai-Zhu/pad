def solution():
    """Manex is a tour bus driver. He has to drive 55 miles to the destination and drive going back to the starting point on a different way that is 10 miles farther. If he can drive 1 mile for 2 minutes and stayed 2 hours at the destination, how long will it take the bus driver to do the entire tour in hours?"""
    # Define the distance to the destination and the distance back to the starting point
    distance_to_dest = 55
    distance_to_start = 65

    # Calculate the total distance traveled by the bus driver
    total_distance = distance_to_dest + distance_to_start

    # Calculate the time it takes to drive 1 mile
    time_per_mile = 2

    # Calculate the total time spent driving
    driving_time = total_distance * time_per_mile / 60

    # Add the time spent at the destination
    total_time = driving_time + 2

    # Convert the total time to hours
    total_time_hours = total_time / 60

    # return the result
    result = total_time_hours
    return result

print(solution())