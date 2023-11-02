def solution():
    jason_children = ["Euneus", "Nebrophonus", "Mermerus", "Pheres"]
    polo_players_per_team = 4
    if len(jason_children) >= polo_players_per_team:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())