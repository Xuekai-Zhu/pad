def solution():
    groups_joined = 9
    players_per_group = 4
    old_players = 2 + 1
    new_players = players_per_group - old_players
    result = new_players * groups_joined + old_players
    return result

print(solution())