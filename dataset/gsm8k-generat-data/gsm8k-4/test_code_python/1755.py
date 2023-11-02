def solution():
    """John gets lost on his way home. His normal trip is 150 miles and would take him 3 hours. He ends up driving 50 miles out of the way and has to get back on track. How long did the trip take if he kept the same speed?"""
    # Define the distance of the normal trip and the distance of the detour
    normal_distance = 150
    detour_distance = 50

    # Calculate the total distance of the trip
    total_distance = normal_distance + detour_distance

    # Calculate the average speed of the trip
    speed = total_distance / 3

    # Calculate the actual travel time of the trip
    actual_distance = normal_distance + detour_distance
    actual_time = actual_distance / speed

    # return the result
    result = actual_time
    return result

print(solution())