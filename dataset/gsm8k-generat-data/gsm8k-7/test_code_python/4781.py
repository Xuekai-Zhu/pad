def solution():
    joseph_speed = 50
    joseph_time = 2.5

    kyle_speed = 62
    kyle_time = 2

    # Calculate the distance Joseph drives
    joseph_distance = joseph_speed * joseph_time

    # Calculate the distance Kyle drives
    kyle_distance = kyle_speed * kyle_time

    # Calculate the difference in distances
    distance_diff = joseph_distance - kyle_distance
    result = distance_diff
    return result

print(solution())