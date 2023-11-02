def solution():
    track_length = 400  # meters

    # Calculate the total time for all three laps
    total_time = 70 + 85 + 85  # seconds

    # Calculate the average time per lap
    average_time_per_lap = total_time / 3

    # Calculate the total distance Bob ran
    total_distance = track_length * 3

    # Calculate the average speed in meters per second
    average_speed = total_distance / total_time
    result = average_speed
    return result

print(solution())