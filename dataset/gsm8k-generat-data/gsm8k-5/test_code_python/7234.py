def solution():
    total_dominoes = 28  # There are 28 dominoes in the set
    total_players = 4  # Jean and her three friends are playing the game

    # Calculate how many dominoes each player will receive
    dominoes_per_player = total_dominoes // total_players

    result = dominoes_per_player
    return result

print(solution())