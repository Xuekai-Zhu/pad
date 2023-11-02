def solution():
    total_distance = 70
    distance_walked_first_day = 20
    distance_walked_third_day = 10

    # Calculate the distance Richard walked the second day
    distance_walked_second_day = 0.5 * (distance_walked_first_day - 6)

    # Calculate the total distance Richard has walked so far
    total_distance_walked = distance_walked_first_day + distance_walked_second_day + distance_walked_third_day

    # Calculate how many miles further Richard has to walk to reach New York City
    distance_left_to_walk = total_distance - total_distance_walked
    result = distance_left_to_walk
    return result

print(solution())