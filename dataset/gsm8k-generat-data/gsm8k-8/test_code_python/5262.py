def solution():
    # Define the distance Fabian has already walked
    distance_walked = 3 * 5

    # Define the remaining distance he needs to cover
    remaining_distance = 30 - distance_walked

    # Calculate how many more hours he needs to walk to cover the remaining distance
    additional_hours = remaining_distance / 5
    result = additional_hours
    return result

print(solution())