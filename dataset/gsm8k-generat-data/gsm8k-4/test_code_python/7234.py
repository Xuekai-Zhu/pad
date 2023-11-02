def solution():
    """Jean and her three friends are playing a game of dominoes. There are 28 dominoes in the set, and Jean wants each player to receive the same number of dominoes. How many dominoes will Jean and her friends each receive?"""
    # Define the number of players and the total number of dominoes
    num_players = 4
    total_dominoes = 28

    # Calculate the number of dominoes each player will receive
    num_dominoes_each = total_dominoes // num_players

    result = num_dominoes_each
    return result

print(solution())