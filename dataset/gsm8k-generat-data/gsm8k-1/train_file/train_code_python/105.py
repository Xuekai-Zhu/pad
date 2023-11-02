def solution():
    """John buys 10 packs of magic cards. Each pack has 20 cards and 1/4 of those cards are uncommon. How many uncommon cards did he get?"""
    packs = 10
    cards_per_pack = 20
    uncommon_percent = 0.25
    uncommon_cards_per_pack = cards_per_pack * uncommon_percent
    total_uncommon_cards = packs * uncommon_cards_per_pack
    result = total_uncommon_cards
    return result

print(solution())