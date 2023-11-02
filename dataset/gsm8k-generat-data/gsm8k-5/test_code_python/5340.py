def solution():
    john_speed = 100 / 13  # John's speed is 100 meters in 13 seconds
    john_acceleration = (john_speed - 4) / 9  # John's acceleration is (final speed - initial speed) / time

    james_initial_speed = 10 / 2  # James' initial speed is 10 meters in 2 seconds
    james_top_speed = john_speed + 2  # James' top speed is 2 m/s faster than John's
    james_acceleration = (james_top_speed - james_initial_speed) / 8  # James' acceleration is (final speed - initial speed) / time

    # Calculate the time it takes James to run 100 meters
    time = (-james_top_speed + ((james_top_speed ** 2) + 4 * 0.5 * 100 / james_acceleration) ** 0.5) / (2 * 0.5 * james_acceleration)
    result = time
    return result

print(solution())