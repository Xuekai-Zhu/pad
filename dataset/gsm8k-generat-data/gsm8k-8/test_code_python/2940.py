def solution():
    # Calculate the time it takes to ascend the mountain
    distance_up = 60
    speed_up = 0.5 * 30
    time_up = distance_up / speed_up

    # Calculate the time it takes to descend the mountain
    distance_down = 72
    speed_down = 1.2 * 30
    time_down = distance_down / speed_down

    # Calculate the total time to pass the whole mountain
    total_time = time_up + time_down
    result = total_time
    return result

print(solution())