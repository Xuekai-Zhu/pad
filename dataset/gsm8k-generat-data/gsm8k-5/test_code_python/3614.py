def solution():
    # Distance between Robin's house and the city center
    total_distance = 500

    # Distance walked from house to where Robin realized he forgot his bag
    first_walk_distance = 200

    # Distance walked from where Robin realized he forgot his bag back to his house
    second_walk_distance = 200

    # Distance walked from Robin's house back to the city center
    third_walk_distance = 500 - first_walk_distance

    # Total distance walked
    distance_walked = first_walk_distance + second_walk_distance + third_walk_distance
    result = distance_walked
    return result

print(solution())