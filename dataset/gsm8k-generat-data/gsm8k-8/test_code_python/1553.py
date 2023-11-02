def solution():
    # Define the number of players in the first half
    first_half_players = 11
    first_half_substitutions = 2

    # Calculate the number of players who played in the first half
    first_half_played = first_half_players + first_half_substitutions

    # Calculate the number of players available for the second half
    available_players = 24 - first_half_played

    # Determine the number of substitutions in the second half
    second_half_substitutions = 2 * first_half_substitutions

    # Calculate the total number of players who played in the game
    total_players_played = first_half_played + second_half_substitutions

    # Calculate the number of players who did not play
    did_not_play = 24 - total_players_played

    result = did_not_play
    return result

print(solution())