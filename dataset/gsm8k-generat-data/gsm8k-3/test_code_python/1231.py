def solution():
    """Two alien spacecraft on a sightseeing tour of Earth left New Orleans airport at 3:00 pm to travel the 448-mile distance to Dallas by air.  Traveling nonstop, the first spacecraft landed in Dallas at 3:30 pm, while the second spacecraft landed in Dallas thirty minutes later. Assuming both spacecraft traveled at constant speed, what was the difference in speed, in miles per hour, between the two spacecraft?"""
    # Calculate the time it took for the first spacecraft to travel from New Orleans to Dallas
    time1 = 0.5  # in hours, since it arrived at 3:30 pm and left at 3:00 pm

    # Calculate the speed of the first spacecraft
    speed1 = 448 / time1

    # Calculate the time it took for the second spacecraft to travel from New Orleans to Dallas
    time2 = 0.5 + 0.5  # in hours, since it arrived 30 minutes later

    # Calculate the speed of the second spacecraft
    speed2 = 448 / time2

    # Calculate the difference in speed between the two spacecraft
    speed_diff = abs(speed1 - speed2)

    # Display the difference in speed
    result = speed_diff
    return result

print(solution())