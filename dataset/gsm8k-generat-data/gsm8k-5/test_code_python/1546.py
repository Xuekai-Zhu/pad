def solution():
    # Time to drive herself to the interview in minutes
    drive_time = (3*60) + 15

    # Time to take the airplane in minutes
    airport_time = 10 + 20  # Driving to the airport and waiting to board
    flight_time = (drive_time / 3) * 60  # One-third of the driving time in minutes
    arrival_time = 10  # Getting off the airplane and arriving at the interview site
    airplane_time = airport_time + flight_time + arrival_time

    # Time saved by taking the airplane in minutes
    time_saved = drive_time - airplane_time

    result = time_saved
    return result

print(solution())