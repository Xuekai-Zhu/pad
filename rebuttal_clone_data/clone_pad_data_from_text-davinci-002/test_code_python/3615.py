def solution():
     games_played = 5
     players_on_team = 11
     avg_hits_per_game = 15
     total_hits = avg_hits_per_game * games_played
     best_player_hits = 25
     other_players_hits = total_hits - best_player_hits
     games_remaining = 6
     other_players_avg_hits_per_game = other_players_hits / (players_on_team - 1)
     other_players_avg_hits_per_game_remaining = other_players_avg_hits_per_game_remaining * games_remaining
     total_avg_hits_per_game = best_player_hits + other_players_avg_hits_per_game_remaining
     result = total_avg_hits_per_game
     return result

print(solution())