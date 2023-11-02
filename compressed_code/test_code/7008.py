def solution():
    
    total_players = 24
    first_half_starters = 11
    first_half_substitutes = 2
    second_half_substitutes = 2 * first_half_substitutes
    total_players_played = first_half_starters + first_half_substitutes + second_half_substitutes
    players_not_played = total_players - total_players_played
    result = players_not_played
    return result

print(solution())