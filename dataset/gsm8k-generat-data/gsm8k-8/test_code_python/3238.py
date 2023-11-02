def solution():
    # Define the distance of the hill and the speeds of running up and down
    distance = 900
    speed_up = 9
    speed_down = 12

    # Calculate the time it takes to run up the hill and down the hill
    time_up = distance / speed_up
    time_down = distance / speed_down

    # Calculate the total time by adding the time up and the time down
    total_time = time_up + time_down
    result = total_time
    return result

print(solution())