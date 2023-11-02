def solution():
    """Two alien spacecraft on a sightseeing tour of Earth left New Orleans airport at 3:00 pm to travel the 448-mile distance to Dallas by air. Traveling nonstop, the first spacecraft landed in Dallas at 3:30 pm, while the second spacecraft landed in Dallas thirty minutes later. Assuming both spacecraft traveled at constant speed, what was the difference in speed, in miles per hour, between the two spacecraft?"""
    distance = 448
    time_first = 0.5  # 30 minutes in hours
    time_second = 1  # 30 minutes more than the first spacecraft
    speed_first = distance / time_first
    speed_second = distance / time_second
    speed_difference = abs(speed_first - speed_second)
    result = speed_difference
    return result

print(solution())