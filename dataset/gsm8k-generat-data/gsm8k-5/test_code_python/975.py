def solution():
    games_played = 0.8 * 20  # John plays in 80% of the 20 games the team plays
    fouls_per_game = 5  # John gets fouled 5 times a game
    shots_per_foul = 2  # John gets 2 shots for every foul
    free_throws_per_game = fouls_per_game * shots_per_foul
    free_throws_per_season = free_throws_per_game * games_played
    free_throws_made = 0.7 * free_throws_per_season  # John hits 70% of his free throws

    result = free_throws_made
    return result

print(solution())