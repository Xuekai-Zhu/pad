def solution():
    # Calculate distance travelled in the first half hour
    distance_first_half_hour = 30 * 0.5

    # Calculate distance travelled in the second half of the trip
    time_second_half = 2 * 0.5  # Twice as long as the first half of the trip
    speed_second_half = 2 * 30  # Twice the speed of the first half of the trip
    distance_second_half = speed_second_half * time_second_half

    # Calculate the total distance driven
    total_distance = distance_first_half_hour + distance_second_half
    result = total_distance
    return result

print(solution())