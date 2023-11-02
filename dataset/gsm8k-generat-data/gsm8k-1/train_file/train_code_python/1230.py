def solution():
    """Two alien spacecraft on a sightseeing tour of Earth left New Orleans airport at 3:00 pm to travel the 448-mile distance to Dallas by air. Traveling nonstop, the first spacecraft landed in Dallas at 3:30 pm, while the second spacecraft landed in Dallas thirty minutes later. Assuming both spacecraft traveled at constant speed, what was the difference in speed, in miles per hour, between the two spacecraft?"""
    distance = 448
    time1 = (30-0)/60.0
    time2 = (60-30)/60.0
    speed1 = distance/time1
    speed2 = distance/time2
    difference_in_speed = abs(speed1 - speed2)
    result = difference_in_speed
    return result

print(solution())