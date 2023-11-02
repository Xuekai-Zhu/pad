def solution():
    bandy_players_per_team = 11
    kate_gosselin_children = 8
    if kate_gosselin_children >= bandy_players_per_team:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())