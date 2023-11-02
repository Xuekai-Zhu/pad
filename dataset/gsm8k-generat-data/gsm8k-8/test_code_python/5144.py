def solution():
    # Define the distances traveled
    south_distance = 40
    east_distance = south_distance + 20
    north_distance = 2 * east_distance

    # Calculate the total distance
    total_distance = south_distance + east_distance + north_distance
    result = total_distance
    return result

print(solution())