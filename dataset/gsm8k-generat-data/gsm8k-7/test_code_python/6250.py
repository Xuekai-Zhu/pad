def solution():
    speed_1 = 60  # mph
    time_1 = 1.5  # hours

    speed_2 = 45  # mph
    time_2 = 2  # hours

    # Calculate the distance Bob traveled in the first leg of his trip
    distance_1 = speed_1 * time_1

    # Calculate the distance Bob traveled in the second leg of his trip
    distance_2 = speed_2 * time_2

    # Calculate the total distance Bob traveled
    total_distance = distance_1 + distance_2
    result = total_distance
    return result

print(solution())