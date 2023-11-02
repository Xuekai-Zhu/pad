def solution():
    # Convert minutes to hours
    run_time = 20 / 60
    walk_time = 30 / 60

    # Calculate the distance of the run and walk
    run_distance = 6 * run_time
    walk_distance = 2 * walk_time

    # Calculate the total distance
    total_distance = run_distance + walk_distance
    result = total_distance
    return result

print(solution())