def solution():
    distance_field = 2000
    time_field = 2 # hours
    distance_track = 10000

    # Calculate Amanda's speed in meters per hour
    speed = distance_field / time_field

    # Calculate the time it will take for Amanda to run the length of the track at the same speed
    time_track = distance_track / speed
    result = time_track
    return result

print(solution())