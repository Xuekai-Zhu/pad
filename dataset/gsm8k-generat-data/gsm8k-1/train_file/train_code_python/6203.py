def solution():
    """The Tigers played 56 home games this year. They had 12 losses and half as many ties. How many games did they win?"""
    total_games = 56
    losses = 12
    ties = losses / 2
    wins = total_games - losses - ties
    result = wins
    return result

print(solution())