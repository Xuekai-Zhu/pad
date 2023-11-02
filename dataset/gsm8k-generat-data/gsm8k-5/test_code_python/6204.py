def solution():
    home_games = 56  # The Tigers played 56 home games
    losses = 12  # The Tigers had 12 losses
    ties = losses / 2  # The Tigers had half as many ties as losses

    # Calculate the number of games the Tigers won
    wins = home_games - losses - ties
    result = wins
    return result

print(solution())