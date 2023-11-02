def solution():
    speed_1 = 80  # mph
    time_1 = 6  # hours

    speed_2 = 60
    time_2 = 4

    speed_3 = 40
    time_3 = 2

    # Calculate the distance covered in each segment
    distance_1 = speed_1 * time_1
    distance_2 = speed_2 * time_2
    distance_3 = speed_3 * time_3

    # Calculate the total distance covered
    total_distance = distance_1 + distance_2 + distance_3
    result = total_distance
    return result

print(solution())