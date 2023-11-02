def solution():
    """If Amanda can run the length of a football field 2000 meters in length in 2 hours, how long would it take her to run the length of a 10000-meter track at the same speed?"""
    # Calculate Amanda's speed in meters per minute
    speed = 2000 / (2 * 60)  # distance/time in meters/minute

    # Calculate the time it would take her to run the 10000-meter track at the same speed
    time = 10000 / speed

    # Display the time in hours and minutes
    hours = int(time / 60)
    minutes = int(time % 60)
    result = f"{hours} hours and {minutes} minutes"
    return result

print(solution())