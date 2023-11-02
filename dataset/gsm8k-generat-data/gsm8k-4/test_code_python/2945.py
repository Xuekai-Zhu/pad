def solution():
    """Polly and Peter play chess. Polly takes an average of 28 seconds per move, while Peter takes an average of 40 seconds per move. The match ends after 30 moves. How many minutes did the match last?"""
    # Define the time taken by Polly and Peter per move in seconds
    polly_time_per_move = 28
    peter_time_per_move = 40

    # Define the number of moves in the match
    moves = 30

    # Calculate the total time taken by Polly and Peter
    total_time = (polly_time_per_move + peter_time_per_move) * moves

    # Convert the total time to minutes
    total_minutes = total_time / 60

    # return the result
    result = total_minutes
    return result

print(solution())