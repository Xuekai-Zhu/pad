def solution():
    # Calculate time to drive
    drive_time = 3 * 60 + 15

    # Calculate time to fly
    airport_time = 10 + 20
    flight_time = drive_time / 3
    landing_time = 10
    fly_time = airport_time + flight_time + landing_time

    # Calculate time saved by flying
    time_saved = drive_time - fly_time

    # Convert time to minutes
    minutes_saved = time_saved % 60
    result = minutes_saved
    return result

print(solution())