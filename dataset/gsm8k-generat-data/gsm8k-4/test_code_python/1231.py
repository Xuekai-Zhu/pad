def solution():
    """Two alien spacecraft on a sightseeing tour of Earth left New Orleans airport at 3:00 pm to travel the 448-mile distance to Dallas by air. Traveling nonstop, the first spacecraft landed in Dallas at 3:30 pm, while the second spacecraft landed in Dallas thirty minutes later. Assuming both spacecraft traveled at constant speed, what was the difference in speed, in miles per hour, between the two spacecraft?"""
    # Define the distance and time taken by the first spacecraft
    distance = 448
    time_1 = 0.5 # in hours

    # Calculate the speed of the first spacecraft
    speed_1 = distance / time_1

    # Calculate the time taken by the second spacecraft
    time_2 = 0.5 + 0.5 # in hours

    # Calculate the speed of the second spacecraft
    speed_2 = distance / time_2

    # Calculate the difference in speed between the two spacecraft
    speed_difference = speed_1 - speed_2

    # Return the result in miles per hour
    result = speed_difference
    return result

print(solution())