def solution():
    initial_games_played = 200
    initial_games_won = (initial_games_played * 63) / 100
    games_played = initial_games_played + 100
    games_won = initial_games_won + 63
    new_percentage = (games_won / games_played) * 100
    result = new_percentage
    return result

print(solution())