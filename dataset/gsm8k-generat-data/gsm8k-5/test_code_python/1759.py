def solution():
    distance_first_second = 6  # Distance between first and second store is 6 miles
    distance_second_third = (2/3)*distance_first_second + distance_first_second  # Distance between second and third store
    total_distance = distance_first_second + distance_second_third + 4 + 4  # Total distance Jason travels
    result = total_distance
    return result

print(solution())