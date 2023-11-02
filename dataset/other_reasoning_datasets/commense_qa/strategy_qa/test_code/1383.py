def solution():
    abba_members = {"male": 2, "female": 2}
    mixed_doubles_teams = {"man": 2, "woman": 2}
    enough_players = all(abba_members[gender] >= mixed_doubles_teams[gender] for gender in mixed_doubles_teams)
    if enough_players:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())