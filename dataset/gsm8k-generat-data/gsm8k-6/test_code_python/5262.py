def solution():
    # Calculate the distance Fabian has already walked
    distance_walked = 3 * 5  # Fabian covers 5 kilometers every hour

    # Calculate how many more kilometers Fabian needs to walk
    remaining_distance = 30 - distance_walked

    # Calculate how many more hours Fabian needs to walk to cover the remaining distance
    hours_to_walk = remaining_distance / 5 

    result = hours_to_walk
    return result

print(solution())