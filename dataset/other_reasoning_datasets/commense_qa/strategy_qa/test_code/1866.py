def solution():
    num_teams = 2
    players_per_team = 5
    total_players_needed = num_teams * players_per_team
    eric_clapton_children = 5
    if eric_clapton_children >= total_players_needed:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())