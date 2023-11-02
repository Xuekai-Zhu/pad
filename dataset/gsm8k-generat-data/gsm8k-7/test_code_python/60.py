def solution():
    num_games_per_daughter = 8
    practice_hours_per_game = 4
    game_hours_per_game = 2

    # Calculate the total number of hours each daughter spends playing and practicing
    total_hours_per_daughter = (num_games_per_daughter * (practice_hours_per_game + game_hours_per_game))

    # Calculate the total number of hours both daughters spend playing and practicing
    total_hours_both_daughters = total_hours_per_daughter * 2

    result = total_hours_both_daughters
    return result

print(solution())