def solution():
    run_speed = 3  # miles per hour
    walk_speed = 1  # mile per hour
    distance = 1  # mile

    # Calculate the time it takes to run half a mile
    time_half_run = 0.5 / run_speed

    # Calculate the time it takes to walk half a mile
    time_half_walk = 0.5 / walk_speed

    # Calculate the total time it takes to travel 1 mile
    total_time = time_half_run + time_half_walk

    # Convert the total time to minutes
    total_time_minutes = total_time * 60
    result = total_time_minutes
    return result

print(solution())