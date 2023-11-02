def solution():
    resistance_time = 20 # in minutes
    walking_distance = 64 # in feet
    walking_speed = 8 # in feet/minute

    # Calculate the time it takes for the cat to walk the given distance
    walking_time = walking_distance / walking_speed

    # Add the resistance time and the walking time to get the total time
    total_time = resistance_time + walking_time
    result = total_time
    return result

print(solution())