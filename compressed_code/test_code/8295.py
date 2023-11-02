def solution():
    
    packs_per_week = 20
    weeks_per_year = 52
    total_packs = packs_per_week * weeks_per_year
    cards_lost = total_packs / 2
    cards_remaining = total_packs - cards_lost
    result = cards_remaining
    return result

print(solution())