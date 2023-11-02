def solution():
     games_played = 40
     games_won = games_played * 0.7
     games_remaining = 10
     games_needed_to_win = games_remaining * 0.6
     games_allowed_to_lose = games_won - games_needed_to_win
     result = games_allowed_to_lose
     return result

print(solution())