def solution():
    """A soccer team had 24 players prepared for a soccer game. The first half saw 11 players start the game with 2 substitutions made. In the second half, the team made twice as many substitutions as it made in the first half. How many players on the team did not play that day?"""
    total_players = 24
    first_half_starters = 11
    first_half_substitutes = 2
    second_half_substitutes = 2 * first_half_substitutes
    total_players_played = first_half_starters + first_half_substitutes + second_half_substitutes
    players_not_played = total_players - total_players_played
    result = players_not_played
    return result

print(solution())