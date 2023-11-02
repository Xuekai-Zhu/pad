def solution():
    """It is Roger’s turn to provide a snack for the baseball team after the game and he has decided to bring trail mix. The trail mix comes in packs of 6 individual pouches. Roger has 13 members on his baseball team, plus 3 coaches and 2 helpers. How many packs of trail mix does he need to buy?"""
    team_members = 13
    coaches = 3
    helpers = 2
    total_people = team_members + coaches + helpers
    pouches_per_pack = 6
    total_pouches_needed = total_people * pouches_per_pack
    result = math.ceil(total_pouches_needed / pouches_per_pack)
    return result

print(solution())