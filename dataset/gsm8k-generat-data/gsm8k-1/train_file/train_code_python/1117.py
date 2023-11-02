def solution():
    """Perry, Dana, Charlie, and Phil played golf together every week. At the end of the season, Perry had won five more games than Dana, but Charlie had won 2 games fewer than Dana. Phil had won 3 games more than Charlie did. If Phil won a total of 12 games, how many more games did Perry win than did Phil?"""
    phil_wins = 12
    charlie_wins = phil_wins - 3
    dana_wins = charlie_wins + 2
    perry_wins = dana_wins + 5
    difference = perry_wins - phil_wins
    result = difference
    return result

print(solution())