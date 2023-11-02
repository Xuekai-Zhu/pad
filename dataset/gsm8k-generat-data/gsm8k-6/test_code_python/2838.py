def solution():
    # Convert all distances to feet and add them up
    distance_Lionel = 4 * 5280  # convert 4 miles to feet
    distance_Esther = 975  # yards to feet
    distance_Niklaus = 1287  # feet
    total_distance = distance_Lionel + distance_Esther + distance_Niklaus
    result = total_distance
    return result

print(solution())