def solution():
    """When doing her exercises, Mairead runs for 40 miles, walks for 3/5 times as many miles as she ran, and walks for five times the number of miles she jogged. Calculate the total distance Mairead has covered while doing her exercises."""
    run_distance = 40
    walk_distance = (3/5) * run_distance
    jog_distance = walk_distance / 5
    total_distance = run_distance + walk_distance + jog_distance
    result = total_distance
    return result

print(solution())