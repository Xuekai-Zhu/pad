def solution():
    # Calculate the distance Bob traveled during the first 1.5 hours
    distance_first_half = 60 * 1.5

    # Calculate the distance Bob traveled during the next 2 hours
    distance_second_half = 45 * 2

    # Calculate the total distance Bob traveled in 3.5 hours
    total_distance = distance_first_half + distance_second_half

    result = total_distance
    return result

print(solution())