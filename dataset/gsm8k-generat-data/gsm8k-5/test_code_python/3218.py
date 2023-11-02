def solution():
    jerry_games = 7  # Jerry won 7 games
    dave_games = jerry_games + 3  # Dave won 3 more games than Jerry
    ken_games = dave_games + 5  # Ken won 5 more games than Dave

    # Calculate the total number of games
    total_games = jerry_games + dave_games + ken_games
    result = total_games
    return result

print(solution())