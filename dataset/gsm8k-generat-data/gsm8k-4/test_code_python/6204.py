def solution():
    """The Tigers played 56 home games this year. They had 12 losses and half as many ties. How many games did they win?"""
    # Define the number of home games played and the number of losses
    home_games = 56
    losses = 12

    # Calculate the number of ties
    ties = losses / 2

    # Calculate the number of wins
    wins = home_games - losses - ties

    # return the result
    result = wins
    return result

print(solution())