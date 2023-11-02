def solution():
    """Tobias went to a swimming pool for 3 hours. Swimming every 100 meters took him 5 minutes, but every 25 minutes he had to take a 5-minute pause. How many meters did Tobias swim during his visit to the swimming pool?"""
    swim_time = 3 * 60  # Convert hours to minutes
    swim_speed = 100 / 5  # 100 meters in 5 minutes
    pause_time = 5
    pause_interval = 25
    total_swim_distance = 0

    for minutes in range(swim_time):
        if minutes % pause_interval == 0 and minutes != 0:
            swim_time -= pause_time
        else:
            total_swim_distance += swim_speed

    result = total_swim_distance
    return result

print(solution())