def solution():
    """A car traveled 360 miles in 4 hours and 30 minutes. What was its speed in miles per hour?"""
    # Convert the time from hours and minutes to just minutes
    time_minutes = 4 * 60 + 30

    # Calculate the speed in miles per minute
    speed = 360 / time_minutes

    # Convert the speed to miles per hour
    speed_mph = speed * 60

    result = speed_mph
    return result

print(solution())