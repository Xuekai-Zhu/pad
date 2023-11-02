def solution():
    
    games_daughter_1 = 8
    games_daughter_2 = 8
    practice_hours_per_game = 4
    game_hours = 2
    hours_daughter_1 = games_daughter_1 * (practice_hours_per_game + game_hours)
    hours_daughter_2 = games_daughter_2 * (practice_hours_per_game + game_hours)
    total_hours = hours_daughter_1 + hours_daughter_2
    result = total_hours
    return result

print(solution())