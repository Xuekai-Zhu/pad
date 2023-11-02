def solution():
    # Calculate John's average speed after the first second
    distance_left = 100 - 4  # John has already run 4 meters
    time_left = 13 - 1  # John has already spent 1 second running 4 meters
    speed = distance_left / time_left

    # Calculate the time it takes for James to run 90 meters at his faster speed
    distance_left = 90 - 10  # James has already run 10 meters
    time_left = (distance_left / (speed + 2)) + 2  # James runs 2 m/s faster than John for the rest of the race
    total_time = time_left + 2  # James took an additional 2 seconds to run the first 10 meters

    # Calculate the total time it takes for James to run 100 meters
    result = total_time
    return result

print(solution())