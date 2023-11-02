def solution():
    lou_distance = 3 # miles
    track_length = 0.25 # miles
    rosie_speed = 2 # times faster than Lou

    # Calculate Lou's speed in miles per minute
    lou_speed = lou_distance / (track_length * 4)

    # Calculate Rosie's speed in miles per minute
    rosie_speed = 2 * lou_speed

    # Calculate the number of times Rosie circles the track in the time it takes Lou to run 3 miles
    rosie_circles = 3 / (track_length * rosie_speed)

    result = rosie_circles
    return result

print(solution())