def solution():
    initial_speed = 30
    distance_up = 60
    distance_down = 72
    up_speed = initial_speed * 0.5
    down_speed = initial_speed * 1.2

    # Calculate the time it takes to ascend
    time_up = distance_up / up_speed

    # Calculate the time it takes to descend
    time_down = distance_down / down_speed

    # Calculate the total time for the whole mountain
    total_time = time_up + time_down
    result = total_time
    return result

print(solution())