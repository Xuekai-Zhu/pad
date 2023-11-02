def solution():
    # Calculate the total time spent walking and playing with the dog each day
    total_walk_play_time = 0.5 * 2  # 0.5 hours per session, twice a day

    # Calculate the time spent feeding the dog each day
    feeding_time = 1/5  # 0.2 hours or 12 minutes

    # Calculate the total time spent on the dog each day
    total_time = total_walk_play_time + feeding_time

    # Convert the time to minutes
    total_time_minutes = total_time * 60
    result = total_time_minutes
    return result

print(solution())