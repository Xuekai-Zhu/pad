def solution():
    """A woman is trying to decide whether it will be quicker to take an airplane or drive herself to a job interview. If she drives herself, the trip will take her 3 hours and 15 minutes. If she takes an airplane, she will first need to drive 10 minutes to the airport, and then wait 20 minutes to board the plane. After that, she will be on the airplane for one-third of the time it would have taken her to drive herself before landing in the destination city. Finally, it will take her an additional 10 minutes to get off the airplane and arrive at her interview site after the plane lands. Given this information, how many minutes faster is it for her to take the airplane?"""
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