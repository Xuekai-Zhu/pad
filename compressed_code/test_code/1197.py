def solution():
    
    drive_time = 3 * 60 + 15
    airport_drive_time = 10
    boarding_time = 20
    flight_time = drive_time / 3
    deboarding_time = 10
    airplane_time = airport_drive_time + boarding_time + flight_time + deboarding_time
    time_saved = drive_time - airplane_time
    result = time_saved
    return result

print(solution())