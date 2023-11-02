def solution():
    # Define the number of players
    num_players = 4

    # Calculate the total number of dominoes
    total_dominoes = 28

    # Divide the total by the number of players to find how many each will receive
    dominoes_per_player = total_dominoes / num_players

    result = dominoes_per_player
    return result

print(solution())