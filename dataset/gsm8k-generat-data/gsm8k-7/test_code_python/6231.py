def solution():
    run_speed = 6  # mph
    run_time = 20 / 60  # hours
    walk_speed = 2  # mph
    walk_time = 30 / 60  # hours

    # Calculate the distance Ms. Warren ran
    run_distance = run_speed * run_time

    # Calculate the distance Ms. Warren walked
    walk_distance = walk_speed * walk_time

    # Calculate the total distance Ms. Warren ran and walked
    total_distance = run_distance + walk_distance
    result = total_distance
    return result

print(solution())