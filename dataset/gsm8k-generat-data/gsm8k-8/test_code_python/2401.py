def solution():
    # Calculate the distance the tiger traveled before zookeepers noticed
    distance_before_noticed = 25 * 3

    # Calculate the distance the tiger traveled before slowing down
    distance_before_slowing = 10 * 4

    # Calculate the distance the tiger traveled while being chased
    distance_while_chased = 50 * 0.5

    # Calculate the total distance the tiger traveled
    total_distance = distance_before_noticed + distance_before_slowing + distance_while_chased

    result = total_distance
    return result

print(solution())