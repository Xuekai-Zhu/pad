def solution():
    """A soccer team had 24 players prepared for a soccer game. The first half saw 11 players start the game with 2 substitutions made. In the second half, the team made twice as many substitutions as it made in the first half. How many players on the team did not play that day?"""
    # Define the initial number of players and the players who started the game
    total_players = 24
    starting_players = 11

    # Calculate the number of players who did not start the game
    non_starting_players = total_players - starting_players

    # Calculate the number of players who played in the first half
    first_half_players = starting_players + 2

    # Calculate the number of substitutions in the first half
    first_half_substitutions = 2
    
    # Calculate the number of substitutions in the second half
    second_half_substitutions = 2 * first_half_substitutions
    
    # Calculate the total number of players who played in the game
    total_playing_players = first_half_players + second_half_substitutions
    
    # Calculate the number of players who did not play
    non_playing_players = total_players - total_playing_players
    
    # return the result
    result = non_playing_players
    return result

print(solution())