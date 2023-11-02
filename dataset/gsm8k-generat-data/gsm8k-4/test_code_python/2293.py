def solution():
    """A boy runs 1.5 km in 45 minutes. What is his speed in kilometers per hour?"""
    # Convert the time from minutes to hours
    time_hours = 45/60

    # Calculate the speed in kilometers per hour
    speed = 1.5 / time_hours

    # Return the result
    result = speed
    return result

print(solution())