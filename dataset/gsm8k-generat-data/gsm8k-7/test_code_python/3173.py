def solution():
    cards_per_pack = 20
    weeks_in_year = 52
    packs_in_year = weeks_in_year * cards_per_pack
    cards_lost_in_fire = packs_in_year / 2
    cards_remaining = packs_in_year - cards_lost_in_fire
    result = cards_remaining
    return result

print(solution())