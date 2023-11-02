def solution():
    # Calculate Amanda's speed in meters per minute
    speed = 2000 / (2*60)

    # Calculate the time it would take Amanda to run 10,000 meters at the same speed
    time = 10000 / speed

    # Convert time from minutes to hours
    time_hours = time / 60

    result = time_hours
    return result

print(solution())