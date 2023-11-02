def solution():
    num_moves = 30
    polly_time_per_move = 28
    peter_time_per_move = 40

    # Calculate the total time for Polly
    polly_time = num_moves * polly_time_per_move

    # Calculate the total time for Peter
    peter_time = num_moves * peter_time_per_move

    # Calculate the total time for the match in seconds
    total_time = polly_time + peter_time

    # Convert seconds to minutes
    total_time_in_minutes = total_time / 60

    result = total_time_in_minutes
    return result

print(solution())