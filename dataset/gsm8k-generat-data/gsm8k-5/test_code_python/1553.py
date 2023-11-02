def solution():
    # Calculate the number of players who played in the first half
    first_half_players = 11 + 2  # 11 started the game and 2 substitutions were made

    # Calculate the number of substitutions made in the second half
    second_half_substitutions = 2 * 2  # Twice as many substitutions as in the first half

    # Calculate the total number of players who played in the second half
    second_half_players = first_half_players - 11 + second_half_substitutions  # The team can only have 11 players on the field at a time

    # Calculate the number of players who did not play in the game
    players_not_played = 24 - second_half_players
    result = players_not_played
    return result

print(solution())