def solution():
    swing_speed = 10  # feet per second
    run_speed = 15  # feet per second
    run_time = 5  # seconds
    swing_time = 10  # seconds

    # Calculate the distance traveled during the running time
    distance_run = run_speed * run_time

    # Calculate the distance traveled during the swinging time
    distance_swing = swing_speed * swing_time

    # Calculate the total distance traveled
    total_distance = distance_run + distance_swing
    result = total_distance
    return result

print(solution())