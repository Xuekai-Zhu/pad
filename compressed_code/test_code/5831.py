def solution():
    
    games_per_daughter = 8
    practice_hours_per_game = 4
    game_hours = 2
    total_games = games_per_daughter * 2 
    total_practice_hours = total_games * practice_hours_per_game
    total_game_hours = total_games * game_hours
    total_hours = total_practice_hours + total_game_hours
    result = total_hours
    return result

print(solution())