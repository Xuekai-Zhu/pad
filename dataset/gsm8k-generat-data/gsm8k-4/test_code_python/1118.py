def solution():
    """Perry, Dana, Charlie, and Phil played golf together every week.  At the end of the season, Perry had won five more games than Dana, but Charlie had won 2 games fewer than Dana.  Phil had won 3 games more than Charlie did.  If Phil won a total of 12 games, how many more games did Perry win than did Phil?"""
    # Let's represent the number of games won by Dana as 'd'
    # According to the problem, Perry won 5 more games than Dana, so Perry won 'd+5' games
    # Charlie won 2 fewer games than Dana, so Charlie won 'd-2' games
    # Phil won 3 more games than Charlie did, so Phil won 'd-2+3 = d+1' games
    # The total number of games won by all four players is the sum of the games won by each player
    #  which is d + (d+5) + (d-2) + (d+1) = 4d + 4

    # We know that Phil won a total of 12 games, so we can solve for 'd' as follows:
    # d + (d+5) + (d-2) + (d+1) = 4d + 4
    # 4d + 4 = 12
    # 4d = 8
    # d = 2

    # Therefore, Dana won 2 games, Perry won 7 games (2+5), Charlie won 0 games (2-2), and Phil won 12 games

    # The difference between the number of games won by Perry and Phil is 7-12 = -5
    # Since Perry won more games than Phil, we can express the answer as the absolute value of the difference
    result = abs(7 - 12)
    return result

print(solution())