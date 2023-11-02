def solution():
    """John buys 10 packs of magic cards. Each pack has 20 cards and 1/4 of those cards are uncommon. How many uncommon cards did he get?"""
    packs = 10
    cards_per_pack = 20
    uncommon_frac = 1/4
    total_cards = packs * cards_per_pack
    uncommon_cards = total_cards * uncommon_frac
    result = uncommon_cards
    return result

print(solution())