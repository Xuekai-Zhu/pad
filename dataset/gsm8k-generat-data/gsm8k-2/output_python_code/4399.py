def solution():
    """Roberto is out for a hike. He travels uphill at 2 MPH and downhill at 3MPH. The trail is 5 miles long. 60% is uphill and the rest is downhill. How long does it take him to complete it in minutes?"""
    total_distance = 5
    uphill_distance = total_distance * 0.6
    downhill_distance = total_distance * 0.4
    uphill_speed = 2
    downhill_speed = 3
    uphill_time = uphill_distance / uphill_speed
    downhill_time = downhill_distance / downhill_speed
    total_time = uphill_time + downhill_time
    result = total_time * 60
    return result

print(solution())