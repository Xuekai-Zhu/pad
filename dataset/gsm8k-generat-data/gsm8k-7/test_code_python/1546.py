def solution():
    drive_time = (3 * 60) + 15  # in minutes
    airport_drive_time = 10
    wait_time = 20
    airplane_time = (drive_time / 3)
    airport_exit_time = 10

    # Calculate total time for airplane trip
    total_airplane_time = airport_drive_time + wait_time + airplane_time + airport_exit_time

    # Calculate the time difference between airplane and driving
    time_difference = drive_time - total_airplane_time
    result = time_difference
    return result

print(solution())