def solution():
    distance = 360
    speed = 60
    stop_time = 1  # in hours

    # Calculate the time taken to drive without stopping
    drive_time = distance / speed

    # Calculate the total time taken including the stop
    total_time = drive_time + stop_time

    result = total_time
    return result

print(solution())