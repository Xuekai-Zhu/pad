def solution():
    """Manex is a tour bus driver. He has to drive 55 miles to the destination and drive going back to the starting point on a different way that is 10 miles farther. If he can drive 1 mile for 2 minutes and stayed 2 hours at the destination, how long will it take the bus driver to do the entire tour in hours?"""
    # Define the distances
    distance_to_destination = 55
    distance_back = 55 + 10

    # Calculate the time to drive to the destination and back
    time_to_destination = distance_to_destination * 2
    time_back = distance_back * 2

    # Calculate the total time for the entire tour
    total_time = (time_to_destination + time_back) / 60

    # Add the time for the 2-hour stay at the destination
    total_time += 2

    result = round(total_time, 2)
    return result

print(solution())