def solution():
    # Calculate the number of winning games played by Sarah
    total_games = 100
    ties = 40
    losses = 30/2  # Sarah loses $2 for every game she loses
    wins = (total_games - ties - losses)
    result = wins
    return result

print(solution())