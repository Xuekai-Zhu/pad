def solution():
    distance_1 = 3
    speed_1 = 150
    distance_2 = 2
    speed_2 = speed_1 + 50
    distance_3 = 1
    speed_3 = 2 * speed_1

    # Calculate the time taken for each distance segment
    time_1 = distance_1 / speed_1
    time_2 = distance_2 / speed_2
    time_3 = distance_3 / speed_3

    # Calculate the total time taken for the entire race
    total_time = time_1 + time_2 + time_3

    # Calculate the average speed for the entire race
    average_speed = 6 / total_time
    result = average_speed
    return result

print(solution())