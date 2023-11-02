def solution():
    
    packs = 10
    cards_per_pack = 20
    uncommon_frac = 1/4
    total_cards = packs * cards_per_pack
    uncommon_cards = total_cards * uncommon_frac
    result = uncommon_cards
    return result

print(solution())