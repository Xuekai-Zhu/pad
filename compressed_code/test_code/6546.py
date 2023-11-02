def solution():
    
    free_throw_percentage = 0.7
    fouls_per_game = 5
    shots_per_foul = 2
    games_played = 20
    games_played_percentage = 0.8
    total_fouls = fouls_per_game * games_played * games_played_percentage
    total_free_throw_attempts = total_fouls * shots_per_foul
    free_throws_made = total_free_throw_attempts * free_throw_percentage
    result = free_throws_made
    
    return result

print(solution())