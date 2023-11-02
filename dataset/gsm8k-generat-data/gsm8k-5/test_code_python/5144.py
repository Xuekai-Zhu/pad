def solution():
    distance_south = 40
    distance_east = distance_south + 20
    distance_north = 2 * distance_east

    # Calculate the total distance
    total_distance = distance_south + distance_east + distance_north
    result = total_distance
    return result

print(solution())