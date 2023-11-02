def solution():
    distance_to_city_center = 500
    distance_walked_before_realizing = 200

    # Calculate the distance Robin walks from his house to the city center and back
    total_distance_walked = 2 * (distance_to_city_center + distance_walked_before_realizing)

    result = total_distance_walked
    return result

print(solution())