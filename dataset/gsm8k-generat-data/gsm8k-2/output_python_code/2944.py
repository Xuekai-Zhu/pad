def solution():
    """Polly and Peter play chess. Polly takes an average of 28 seconds per move, while Peter takes an average of 40 seconds per move. The match ends after 30 moves. How many minutes did the match last?"""
    polly_time_per_move = 28
    peter_time_per_move = 40
    total_moves = 30
    total_time = (polly_time_per_move + peter_time_per_move) * total_moves
    total_time_in_minutes = total_time / 60
    result = total_time_in_minutes
    return result

print(solution())