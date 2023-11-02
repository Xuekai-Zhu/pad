def solution():
    # Calculate the distance Kevin traveled at different speeds and add them up
    distance_1 = 10 * 0.5  # Kevin ran at 10 miles per hour for half an hour
    distance_2 = 20 * 0.5  # Kevin ran at 20 miles per hour for half an hour
    distance_3 = 8 * 0.25  # Kevin ran at 8 miles per hour for 15 minutes (0.25 hours)
    total_distance = distance_1 + distance_2 + distance_3  # Add up the distances traveled at different speeds
    result = total_distance
    return result

print(solution())