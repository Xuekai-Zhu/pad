def solution():
    """When doing her exercises, Mairead runs for 40 miles, walks for 3/5 times as many miles as she ran, and walks for five times the number of miles she jogged. Calculate the total distance Mairead has covered while doing her exercises."""
    # Define the distance Mairead runs
    run_distance = 40

    # Calculate the distance Mairead walks
    walk_distance = (3/5) * run_distance

    # Calculate the distance Mairead jogs
    jog_distance = walk_distance / 5

    # Calculate the total distance Mairead covers
    total_distance = run_distance + walk_distance + jog_distance

    # Display the total distance
    result = total_distance
    return result

print(solution())