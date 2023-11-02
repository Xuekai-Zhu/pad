def solution():
    """The Tigers played 56 home games this year. They had 12 losses and half as many ties. How many games did they win?"""
    # Define the number of losses and ties
    losses = 12
    ties = losses / 2

    # Calculate the number of wins
    wins = 56 - losses - ties

    # Display the number of wins
    result = wins
    return result

print(solution())