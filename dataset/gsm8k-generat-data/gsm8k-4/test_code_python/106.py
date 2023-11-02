def solution():
    """John buys 10 packs of magic cards. Each pack has 20 cards and 1/4 of those cards are uncommon. How many uncommon cards did he get?"""
    # Define the total number of packs and cards per pack
    total_packs = 10
    cards_per_pack = 20

    # Calculate the total number of cards
    total_cards = total_packs * cards_per_pack

    # Calculate the number of uncommon cards
    uncommon_cards = total_cards * (1/4)

    # return the result
    result = uncommon_cards
    return result

print(solution())