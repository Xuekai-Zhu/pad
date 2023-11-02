def solution():
    track1_distance = 200
    track1_speed = 50

    track2_distance = 240
    track2_speed = 80

    # Calculate the time taken for the first train
    time1 = track1_distance / track1_speed

    # Calculate the time taken for the second train
    time2 = track2_distance / track2_speed

    # Calculate the average time taken
    average_time = (time1 + time2) / 2

    # Round the average time to the nearest integer
    result = round(average_time)
    return result

print(solution())