def solution():
    distance_up = 60  # distance going up the mountain
    distance_down = 72  # distance going down the mountain
    speed = 30  # original speed of the vehicle

    # Calculate the new speeds after ascending and descending the mountain
    speed_up = speed * 0.5  # speed decreases by 50% when ascending
    speed_down = speed * 1.2  # speed increases by 20% when descending

    # Calculate the time it takes to go up and down the mountain
    time_up = distance_up / speed_up
    time_down = distance_down / speed_down

    # Calculate the total time it takes to pass the whole mountain
    total_time = time_up + time_down
    result = total_time
    return result

print(solution())