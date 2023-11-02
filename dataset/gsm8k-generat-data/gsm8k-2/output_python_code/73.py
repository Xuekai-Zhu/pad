def solution():
    """It is Roger’s turn to provide a snack for the baseball team after the game and he has decided to bring trail mix. The trail mix comes in packs of 6 individual pouches. Roger has 13 members on his baseball team, plus 3 coaches and 2 helpers. How many packs of trail mix does he need to buy?"""
    total_people = 13 + 3 + 2
    pouches_per_pack = 6
    total_pouches_needed = total_people // pouches_per_pack
    if total_people % pouches_per_pack != 0:
        total_pouches_needed += 1
    packs_needed = total_pouches_needed / pouches_per_pack
    result = packs_needed
    return result

print(solution())