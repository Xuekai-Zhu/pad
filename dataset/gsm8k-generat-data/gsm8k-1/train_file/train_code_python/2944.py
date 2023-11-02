def solution():
    """Polly and Peter play chess. Polly takes an average of 28 seconds per move, while Peter takes an average of 40 seconds per move. The match ends after 30 moves. How many minutes did the match last?"""
    moves = 30
    polly_time = moves * 28
    peter_time = moves * 40
    total_time = (polly_time + peter_time) / 60
    result = total_time
    return result

print(solution())