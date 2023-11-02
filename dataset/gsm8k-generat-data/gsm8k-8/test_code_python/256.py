def solution():
    # Define the scale on the map
    scale = 1/4

    # Define the distance between the points on the map
    map_distance = 3 + 3/8

    # Calculate the actual distance between the towns
    actual_distance = map_distance / scale * 8

    result = actual_distance
    return result

print(solution())