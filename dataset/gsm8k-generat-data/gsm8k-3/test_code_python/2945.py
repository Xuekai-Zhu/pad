def solution():
    """Polly and Peter play chess. Polly takes an average of 28 seconds per move, while Peter takes an average of 40 seconds per move. The match ends after 30 moves. How many minutes did the match last?"""
    # Define the average time per move for Polly and Peter, in seconds
    POLLY_TIME = 28
    PETER_TIME = 40

    # Define the total number of moves in the match
    TOTAL_MOVES = 30

    # Calculate the total time for all of Polly's moves
    polly_total_time = POLLY_TIME * TOTAL_MOVES

    # Calculate the total time for all of Peter's moves
    peter_total_time = PETER_TIME * TOTAL_MOVES

    # Calculate the total time for the entire match, in seconds
    total_time = polly_total_time + peter_total_time

    # Convert the total time to minutes
    total_minutes = total_time / 60

    # Display the total time in minutes
    result = total_minutes
    return result

print(solution())