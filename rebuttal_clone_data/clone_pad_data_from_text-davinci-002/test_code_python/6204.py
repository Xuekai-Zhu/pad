def solution():
    home_games = 56
    losses = 12
    ties = losses / 2
    wins = home_games - losses - ties
    result = wins
    return result

print(solution())