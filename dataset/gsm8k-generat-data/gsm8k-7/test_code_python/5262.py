def solution():
    distance_per_hour = 5
    hours_walked = 3
    total_distance = 30

    # Calculate the distance Fabian has already walked
    distance_walked = distance_per_hour * hours_walked

    # Calculate the remaining distance Fabian needs to walk
    remaining_distance = total_distance - distance_walked

    # Calculate the number of hours needed to walk the remaining distance
    hours_needed = remaining_distance / distance_per_hour
    result = hours_needed
    return result

print(solution())