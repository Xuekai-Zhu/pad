def solution():
    """John buys 10 packs of magic cards. Each pack has 20 cards and 1/4 of those cards are uncommon. How many uncommon cards did he get?"""
    packs_bought = 10
    cards_per_pack = 20
    percentage_uncommon = 25 # 25% = 1/4
    total_cards = packs_bought * cards_per_pack
    uncommon_cards = total_cards * (percentage_uncommon / 100)
    result = uncommon_cards
    return result

print(solution())