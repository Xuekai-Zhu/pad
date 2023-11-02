def solution():
    """A monkey swings from branch to branch at an average distance of 1.2 meters per second. How far will a monkey swing in meters if it consistently swings from branches for 30 minutes?"""
    swing_speed = 1.2  # meters per second
    time_in_minutes = 30
    time_in_seconds = time_in_minutes * 60
    distance = swing_speed * time_in_seconds
    result = distance
    return result

print(solution())