def solution():
    
    packs = 10
    cards_per_pack = 20
    uncommon_percent = 0.25
    uncommon_cards_per_pack = cards_per_pack * uncommon_percent
    total_uncommon_cards = packs * uncommon_cards_per_pack
    result = total_uncommon_cards
    return result

print(solution())