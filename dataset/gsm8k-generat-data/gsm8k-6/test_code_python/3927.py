def solution():
    # Calculate the time taken to run for half a mile
    time_to_run_half_mile = 0.5 / 3  # Cindy can run at 3 miles per hour

    # Calculate the time taken to walk for half a mile
    time_to_walk_half_mile = 0.5 / 1  # Cindy can walk at 1 mile per hour

    # Calculate the total time taken to travel 1 mile
    total_time = time_to_run_half_mile + time_to_walk_half_mile

    # Convert the total time to minutes
    total_time_in_minutes = total_time * 60

    result = total_time_in_minutes
    return result

print(solution())