def solution():
    """Bill has played 200 games of poker and won 63% of them. If he plays 100 more games and loses 43 of them, what is his new win percentage?"""
    games_played = 200 + 100
    games_won = 0.63 * 200 + (100-43)
    win_percentage = games_won / games_played * 100
    result = win_percentage
    return result

print(solution())