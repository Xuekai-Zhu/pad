def solution():
    # Calculate the number of dominoes each person will receive
    num_players = 4  # Jean and her three friends
    dominoes_per_player = 28 // num_players  # integer division to evenly distribute the dominoes
    result = dominoes_per_player
    return result

print(solution())