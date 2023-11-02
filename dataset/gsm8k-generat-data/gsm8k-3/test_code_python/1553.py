def solution():
    """A soccer team had 24 players prepared for a soccer game. The first half saw 11 players start the game with 2 substitutions made.
    In the second half, the team made twice as many substitutions as it made in the first half. How many players on the team did not play that day?"""
    # Define the total number of players
    total_players = 24

    # Calculate the number of players who played in the first half
    first_half_players = 11 + 2

    # Calculate the number of substitutions in the first half
    first_half_subs = 2

    # Calculate the number of substitutions in the second half
    second_half_subs = 2 * first_half_subs

    # Calculate the total number of players who played in the game
    total_played = first_half_players + second_half_subs

    # Calculate the number of players who did not play
    not_played = total_players - total_played

    # Display the number of players who did not play
    result = not_played
    return result

print(solution())