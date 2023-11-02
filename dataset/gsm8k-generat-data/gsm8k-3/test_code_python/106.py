def solution():
    """John buys 10 packs of magic cards. Each pack has 20 cards and 1/4 of those cards are uncommon. How many uncommon cards did he get?"""
    # Define the number of packs bought and the number of cards per pack
    packs = 10
    cards_per_pack = 20

    # Calculate the total number of cards
    total_cards = packs * cards_per_pack

    # Calculate the number of uncommon cards
    uncommon_cards = total_cards * (1/4)

    # Return the number of uncommon cards
    result = uncommon_cards
    return result

print(solution())