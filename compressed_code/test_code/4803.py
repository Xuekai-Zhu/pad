def solution():
    
    total_games = 56
    losses = 12
    ties = losses / 2
    wins = total_games - losses - ties
    result = wins
    return result

print(solution())