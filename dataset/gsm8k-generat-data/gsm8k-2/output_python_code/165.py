def solution():
    """Manex is a tour bus driver. He has to drive 55 miles to the destination and drive going back to the starting point on a different way that is 10 miles farther. If he can drive 1 mile for 2 minutes and stayed 2 hours at the destination, how long will it take the bus driver to do the entire tour in hours?"""
    distance_to_destination = 55
    distance_to_starting_point = distance_to_destination + 10
    total_distance = distance_to_destination + distance_to_starting_point
    driving_time = (total_distance * 2) / 60
    total_time = driving_time + 2
    result = total_time
    return result

print(solution())