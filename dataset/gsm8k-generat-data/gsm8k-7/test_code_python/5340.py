def solution():
    john_speed = 100 / 13  # in meters per second
    john_acceleration = john_speed - 4  # in meters per second^2
    james_acceleration = john_acceleration  # assuming James maintains the same acceleration as John

    # Calculate James' speed at top speed
    james_speed_top = john_speed + 2  # in meters per second

    # Calculate James' time to cover the first 10 meters
    james_time_first_10 = 2  # in seconds

    # Calculate James' acceleration time to reach top speed
    james_time_accelerate = (james_speed_top - 0) / james_acceleration  # in seconds

    # Calculate James' time to cover the remaining 90 meters at top speed
    james_time_top_speed = 90 / james_speed_top  # in seconds 

    # Calculate James' total time to cover 100 meters
    james_total_time = james_time_first_10 + james_time_accelerate + james_time_top_speed  # in seconds
    result = james_total_time
    return result

print(solution())