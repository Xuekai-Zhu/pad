def solution():
    # Calculate the time it took for Skye to drive the first 3 kilometers
    time_first_3km = 3 / 150

    # Calculate the speed for the next 2 kilometers
    speed_next_2km = 150 + 50  # Skye's speed was 50 more than the first 3 kilometers

    # Calculate the time it took for Skye to drive the next 2 kilometers
    time_next_2km = 2 / speed_next_2km

    # Calculate the speed for the last 1 kilometer
    speed_last_1km = 2 * 150  # Skye's speed was twice as fast as the first 3 kilometers

    # Calculate the time it took for Skye to drive the last 1 kilometer
    time_last_1km = 1 / speed_last_1km

    # Calculate the total time it took for Skye to complete the race
    total_time = time_first_3km + time_next_2km + time_last_1km

    # Calculate the average speed for the entire race
    average_speed = 6 / total_time
    result = average_speed
    return result

print(solution())