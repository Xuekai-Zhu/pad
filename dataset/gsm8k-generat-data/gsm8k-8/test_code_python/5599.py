def solution():
    # Calculate the distance covered while running
    run_distance = 40

    # Calculate the distance covered while walking
    walk_distance = (3/5) * run_distance + 5 * (run_distance - walk_distance)

    # Calculate the total distance covered
    total_distance = run_distance + walk_distance

    result = total_distance
    return result

print(solution())