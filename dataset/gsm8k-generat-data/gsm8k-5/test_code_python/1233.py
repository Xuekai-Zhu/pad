def solution():
    time_1 = 0.5  # Kevin ran at 10 miles per hour for half an hour
    time_2 = 0.5  # Kevin ran at 20 miles per hour for half an hour
    time_3 = 0.25  # Kevin ran at 8 miles per hour for 15 minutes (0.25 hours)
    speed_1 = 10  # Kevin ran at 10 miles per hour
    speed_2 = 20  # Kevin ran at 20 miles per hour
    speed_3 = 8  # Kevin ran at 8 miles per hour

    # Calculate the distance Kevin ran at each speed
    distance_1 = speed_1 * time_1
    distance_2 = speed_2 * time_2
    distance_3 = speed_3 * time_3

    # Calculate the total distance Kevin ran
    total_distance = distance_1 + distance_2 + distance_3
    result = total_distance
    return result

print(solution())