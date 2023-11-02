def solution():
    """Phil likes to collect baseball cards. He buys a pack of twenty each week for a year, but then loses half of them one day in a fire. How many baseball cards does Phil have left?"""
    packs_per_week = 20
    weeks_per_year = 52
    total_packs = packs_per_week * weeks_per_year
    cards_lost = total_packs / 2
    cards_remaining = total_packs - cards_lost
    result = cards_remaining
    return result

print(solution())