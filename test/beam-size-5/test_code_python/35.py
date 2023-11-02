def solution():
    run_speed = 3  # Dana can run at a rate of 3 miles per hour
    walk_speed = run_speed / 2  # Dana can walk at a rate of speed that is half as fast as she can run
    running_time = 6 / 3  # Dana spends one-third of the time running
    walking_time = 6 / 3  # Dana spends two-thirds of the time walking

    # Calculate the distance Dana can run in 6 hours
    run_distance = run_speed * running_time

    # Calculate the distance Dana can walk in 6 hours
    walk_distance = walk_speed * walking_time

    # Calculate the total distance Dana can travel in 6 hours
    total_distance = run_distance + walk_distance
    result = total_distance
    return result

print(solution())