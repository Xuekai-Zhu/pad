def solution():
    """A boy runs 1.5 km in 45 minutes. What is his speed in kilometers per hour?"""
    # Convert minutes to hours
    time_hours = 45 / 60

    # Calculate speed in kilometers per hour
    speed_kph = 1.5 / time_hours

    # Display the speed
    result = speed_kph
    return result

print(solution())