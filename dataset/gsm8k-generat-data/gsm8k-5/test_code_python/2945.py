def solution():
    polly_time = 28 * 30  # Polly takes 28 seconds per move, and there are 30 moves
    peter_time = 40 * 30  # Peter takes 40 seconds per move, and there are 30 moves

    # Calculate the total time for the match in seconds
    total_time = polly_time + peter_time

    # Convert the total time to minutes
    total_time_minutes = total_time / 60
    result = total_time_minutes
    return result

print(solution())