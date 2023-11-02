def solution():
    
    games_per_daughter = 8
    practice_time_per_game = 4
    game_time = 2
    total_games = games_per_daughter * 2
    total_practice_time = total_games * practice_time_per_game
    total_game_time = total_games * game_time
    total_time = total_game_time + total_practice_time
    result = total_time
    return result

print(solution())