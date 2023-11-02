def solution():
    """John hits 70% of his free throws. For every foul he gets 2 shots. He gets fouled 5 times a game. How many free throws does he get if he plays in 80% of the 20 games the team plays?"""
    free_throw_percentage = 0.7
    fouls_per_game = 5
    shots_per_foul = 2
    games_played = 20
    games_played_percentage = 0.8
    total_fouls = fouls_per_game * games_played * games_played_percentage
    total_free_throws = total_fouls * shots_per_foul * free_throw_percentage
    result = total_free_throws
    return result

print(solution())