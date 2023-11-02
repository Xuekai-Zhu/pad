def solution():
     games_played = 15
     games_remaining = 20 - games_played
     points_scored = 26 * games_played
     points_needed = 30 * 20
     points_per_game_needed = (points_needed - points_scored) / games_remaining
     result = points_per_game_needed
     return result

print(solution())