def solution():
    swimming_time = 3 * 60  # convert 3 hours to minutes
    swim_distance = 100  # in meters
    swim_time_per_100m = 5  # in minutes
    pause_time = 5  # in minutes
    pause_interval = 25  # in minutes

    total_swim_distance = 0
    current_time = 0
    while current_time < swimming_time:
        current_time += swim_time_per_100m
        total_swim_distance += swim_distance
        if current_time % pause_interval == 0:
            current_time += pause_time

    result = total_swim_distance
    return result

print(solution())