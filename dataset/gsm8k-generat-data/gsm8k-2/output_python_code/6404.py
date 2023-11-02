def solution():
    """Tobias went to a swimming pool for 3 hours. Swimming every 100 meters took him 5 minutes, but every 25 minutes he had to take a 5-minute pause. How many meters did Tobias swim during his visit to the swimming pool?"""
    total_time = 180  # 3 hours in minutes
    swim_distance = 100
    swim_time = 5
    pause_time = 5
    pause_interval = 25
    total_swim_time = 0
    total_swim_distance = 0

    for i in range(total_time):
        if i % pause_interval == 0 and i != 0:
            total_swim_time += pause_time
        else:
            total_swim_time += swim_time

        if total_swim_time >= swim_time:
            total_swim_time -= swim_time
            total_swim_distance += swim_distance

    result = total_swim_distance
    return result

print(solution())