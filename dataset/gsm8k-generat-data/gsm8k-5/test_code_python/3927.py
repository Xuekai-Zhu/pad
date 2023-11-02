def solution():
    run_speed = 3  # Cindy can run at 3 miles per hour
    walk_speed = 1  # Cindy can walk at 1 mile per hour
    distance = 1  # Cindy needs to travel 1 mile
    run_distance = 0.5  # Cindy runs half a mile
    walk_distance = 0.5  # Cindy walks half a mile

    # Calculate the time it takes Cindy to run half a mile
    run_time = run_distance / run_speed

    # Calculate the time it takes Cindy to walk half a mile
    walk_time = walk_distance / walk_speed

    # Calculate the total time it takes Cindy to travel 1 mile
    total_time = run_time + walk_time

    # Convert the total time to minutes
    total_minutes = total_time * 60
    result = total_minutes
    return result

print(solution())