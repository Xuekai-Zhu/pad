def solution():
    # Define the number of packs and cards per pack
    packs = 10
    cards_per_pack = 20
    
    # Calculate the total number of cards and the number of uncommon cards
    total_cards = packs * cards_per_pack
    uncommon_cards = total_cards * (1/4)
    result = uncommon_cards
    return result

print(solution())