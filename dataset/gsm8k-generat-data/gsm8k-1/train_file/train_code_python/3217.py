def solution():
    """Ken, Dave, and Jerry played shuffleboard against one another while together vacationing in Florida. Ken won 5 more games than Dave, and Dave won 3 more games than Jerry. If Jerry won 7 games, what was the total number of games they played?"""
    jerry_wins = 7
    dave_wins = jerry_wins + 3
    ken_wins = dave_wins + 5
    total_games = jerry_wins + dave_wins + ken_wins
    result = total_games
    return result

print(solution())