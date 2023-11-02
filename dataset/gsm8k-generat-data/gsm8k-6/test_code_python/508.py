def solution():
    # Calculate the distance James drove in the first half hour
    distance_half_hour = 0.5 * 30  # Distance = speed x time

    # Calculate the distance James drove in the second half of his journey
    time_second_half = 2 * 0.5  # Twice as long as the first half
    speed_second_half = 2 * 30  # Twice the speed
    distance_second_half = time_second_half * speed_second_half

    # Calculate the total distance James drove
    total_distance = distance_half_hour + distance_second_half
    result = total_distance
    return result

print(solution())