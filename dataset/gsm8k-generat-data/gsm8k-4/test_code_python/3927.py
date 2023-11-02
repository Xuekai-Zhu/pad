def solution():
    """Cindy can run at 3 miles per hour and walk at 1 mile per hour. If she runs for half a mile and then walks for half a mile, how many minutes will it take her to travel the full mile?"""
    # Define the distance Cindy runs and walks
    run_distance = 0.5
    walk_distance = 0.5

    # Calculate the time it takes Cindy to run and walk each distance
    run_time = run_distance / 3.0  # 3 mph equals 1 mile in 1/3 hour
    walk_time = walk_distance / 1.0  # 1 mph equals 1 mile in 1 hour

    # Calculate the total time it takes Cindy to travel the full mile
    total_time = run_time + walk_time

    # Convert the total time to minutes
    total_time = total_time * 60

    result = total_time
    return result

print(solution())