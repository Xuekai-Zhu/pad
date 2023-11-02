def solution():
     archibalds_games_won = 12
     brothers_games_won = 18
     total_games_played = archibalds_games_won + brothers_games_won
     archibalds_win_percentage = (archibalds_games_won / total_games_played) * 100
     result = archibalds_win_percentage
     return result

print(solution())