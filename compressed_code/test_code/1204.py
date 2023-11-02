def solution():
    
    total_players = 24
    first_half_starters = 11
    first_half_subs = 2
    second_half_subs = 2 * first_half_subs
    total_subs = first_half_subs + second_half_subs
    total_starters = first_half_starters + total_subs
    players_not_played = total_players - total_starters
    result = players_not_played
    return result

print(solution())