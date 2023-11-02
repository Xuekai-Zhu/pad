def solution():
    num_players = 4
    total_dominoes = 28

    # Calculate the number of dominoes each player will receive by dividing the total number of dominoes by the number of players
    dominoes_per_player = total_dominoes / num_players
    result = dominoes_per_player
    return result

print(solution())