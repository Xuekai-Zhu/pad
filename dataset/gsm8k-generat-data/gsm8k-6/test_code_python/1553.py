def solution():
    # Calculate the number of players who played in the first half
    first_half_players = 11 + 2  # 11 players started the game with 2 substitutions made

    # Calculate the number of substitutions in the first half
    first_half_subs = 2

    # Calculate the number of substitutions in the second half
    second_half_subs = 2 * first_half_subs  # second half had twice as many substitutions as the first half

    # Calculate the total number of players who played in the game
    total_players_played = first_half_players + second_half_subs

    # Calculate the number of players who did not play
    players_not_played = 24 - total_players_played

    result = players_not_played
    return result

print(solution())