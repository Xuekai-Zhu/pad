def solution():
     games_given = 6
     games_received = 7
     games_held = games_received + games_given
     games_ratio = games_held / games_given
     result = games_ratio * games_given
     return result

print(solution())