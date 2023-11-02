def solution():
    """Roberto is out for a hike. He travels uphill at 2 MPH and downhill at 3MPH. The trail is 5 miles long. 60% is uphill and the rest is downhill. How long does it take him to complete it in minutes?"""
    total_miles = 5
    uphill_percent = 60
    downhill_percent = 100 - uphill_percent
    uphill_miles = total_miles * (uphill_percent / 100)
    downhill_miles = total_miles - uphill_miles
    uphill_time = uphill_miles / 2
    downhill_time = downhill_miles / 3
    total_time = uphill_time + downhill_time
    total_time_in_minutes = total_time * 60
    result = total_time_in_minutes
    return result

print(solution())