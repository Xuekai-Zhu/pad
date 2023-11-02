def solution():
    # Define the minimum number of players needed to play Dungeons and Dragons
    min_players = 3
    # Determine if the game is well suited for solo play
    if min_players > 1:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())