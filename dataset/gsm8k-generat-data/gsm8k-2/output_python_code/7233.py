def solution():
    """Jean and her three friends are playing a game of dominoes. There are 28 dominoes in the set, and Jean wants each player to receive the same number of dominoes. How many dominoes will Jean and her friends each receive?"""
    total_dominoes = 28
    num_players = 4
    dominoes_per_player = total_dominoes // num_players
    result = dominoes_per_player
    return result

print(solution())