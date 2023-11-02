def solution():
    """James drives 30 mph for half an hour and then twice as long for twice the speed. How far did he drive in total?"""
    # Define the initial speed and time
    speed_1 = 30
    time_1 = 0.5

    # Define the second speed and time
    speed_2 = speed_1 * 2
    time_2 = time_1 * 2

    # Calculate the distances
    distance_1 = speed_1 * time_1
    distance_2 = speed_2 * time_2

    # Calculate the total distance
    total_distance = distance_1 + distance_2

    result = total_distance
    return result

print(solution())