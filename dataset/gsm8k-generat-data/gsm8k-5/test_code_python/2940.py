def solution():
    distance_up = 60  # Distance going to the top of the mountain
    distance_down = 72  # Distance going down to the foot of the mountain

    # Calculate the time taken to ascend the mountain
    speed_up = 0.5 * 30  # Decreased speed by 50 percent
    time_up = distance_up / speed_up

    # Calculate the time taken to descend the mountain
    speed_down = 1.2 * 30  # Increased speed by 20 percent
    time_down = distance_down / speed_down

    # Total time taken to pass the whole mountain
    total_time = time_up + time_down
    result = total_time
    return result

print(solution())