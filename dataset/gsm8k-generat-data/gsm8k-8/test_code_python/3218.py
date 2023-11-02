def solution():
    # Jerry won 7 games
    jerry_wins = 7

    # Dave won 3 more games than Jerry
    dave_wins = jerry_wins + 3

    # Ken won 5 more games than Dave
    ken_wins = dave_wins + 5

    # Total number of games played is the sum of all three players' wins
    total_games = jerry_wins + dave_wins + ken_wins
    result = total_games
    return result

print(solution())