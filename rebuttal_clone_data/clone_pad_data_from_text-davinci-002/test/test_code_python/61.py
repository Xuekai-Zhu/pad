def solution():
    
    packs_bought = 10
    cards_per_pack = 20
    percentage_uncommon = 25 # 25% = 1/4
    total_cards = packs_bought * cards_per_pack
    uncommon_cards = total_cards * (percentage_uncommon / 100)
    result = uncommon_cards
    return result

print(solution())