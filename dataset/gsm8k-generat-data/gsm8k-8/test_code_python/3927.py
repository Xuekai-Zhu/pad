def solution():
    # Calculate the time it takes Cindy to run half a mile
    run_time = 0.5 / 3

    # Calculate the time it takes Cindy to walk half a mile
    walk_time = 0.5 / 1

    # Calculate the total time it takes Cindy to travel one mile
    total_time = run_time + walk_time

    # Convert the total time to minutes
    total_time_minutes = total_time * 60

    result = total_time_minutes
    return result

print(solution())