def solution():
    cosmic_girls_members = 13
    players_per_team = 5
    total_players_needed = 2 * players_per_team
    if cosmic_girls_members >= total_players_needed:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())