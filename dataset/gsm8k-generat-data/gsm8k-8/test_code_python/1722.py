def solution():
    # Calculate the time taken for the first 3 kilometers
    time1 = 3 / 150

    # Calculate the time taken for the next 2 kilometers
    speed2 = 150 + 50
    time2 = 2 / speed2

    # Calculate the time taken for the last 1 kilometer
    speed3 = 2 * 150
    time3 = 1 / speed3

    # Calculate the total time taken for the race
    total_time = time1 + time2 + time3

    # Calculate the average speed for the entire race
    average_speed = 6 / total_time
    result = average_speed
    return result

print(solution())