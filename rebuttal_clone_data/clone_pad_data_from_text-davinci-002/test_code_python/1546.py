def solution():
    driving_time = 195
    airport_drive_time = 10
    wait_time = 20
    flight_time = (driving_time / 3)
    post_flight_time = 10

    total_drive_time = airport_drive_time + driving_time + post_flight_time
    total_flight_time = airport_drive_time + wait_time + flight_time + post_flight_time

    difference_in_time = total_drive_time - total_flight_time
    result = difference_in_time
    return result

print(solution())