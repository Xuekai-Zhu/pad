def solution():
    bath_time = 20 # minutes
    drying_time = bath_time / 2 # half as long as bath time
    walking_distance = 3 # miles
    walking_speed = 6 # miles per hour

    # Convert walking distance to time
    walking_time = walking_distance / walking_speed * 60 # minutes

    # Calculate total time spent with dog
    total_time = bath_time + drying_time + walking_time
    result = total_time
    return result

print(solution())