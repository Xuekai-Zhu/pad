def solution():
    packs_of_cards = 10  # John buys 10 packs of magic cards
    cards_per_pack = 20  # Each pack has 20 cards
    uncommon_cards_ratio = 1/4  # 1/4 of the cards in each pack are uncommon

    # Calculate the total number of cards and the total number of uncommon cards
    total_cards = packs_of_cards * cards_per_pack
    uncommon_cards = total_cards * uncommon_cards_ratio
    result = uncommon_cards
    return result

print(solution())