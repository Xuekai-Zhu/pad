def solution():
    distance = 3  # kilometers
    time = 2  # hours

    # Convert kilometers to meters
    distance_m = distance * 1000

    # Convert hours to minutes
    time_mins = time * 60

    # Calculate speed in meters per minute
    speed = distance_m / time_mins
    result = speed
    return result

print(solution())