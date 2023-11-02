def solution():
    # Calculate Troy's total distance
    troy_distance = 2 * 75

    # Calculate Emily's total distance
    emily_distance = 2 * 98

    # Calculate the difference in distance between Troy and Emily
    distance_difference = emily_distance - troy_distance

    # Calculate the total distance Emily walks in five days
    total_emily_distance = emily_distance * 5

    # Calculate the total distance Troy walks in five days
    total_troy_distance = troy_distance * 5

    # Calculate the difference in distance between Emily and Troy in five days
    total_distance_difference = total_emily_distance - total_troy_distance

    result = total_distance_difference
    return result

print(solution())