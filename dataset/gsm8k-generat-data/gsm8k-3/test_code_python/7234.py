def solution():
    """Jean and her three friends are playing a game of dominoes. There are 28 dominoes in the set, and Jean wants each player to receive the same number of dominoes. How many dominoes will Jean and her friends each receive?"""
    # Define the number of players and the total number of dominoes
    NUM_PLAYERS = 4
    TOTAL_DOMINOES = 28

    # Calculate the number of dominoes each player will receive
    dominoes_per_player = TOTAL_DOMINOES // NUM_PLAYERS

    # Display the number of dominoes each player will receive
    result = dominoes_per_player
    return result

print(solution())