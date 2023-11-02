def solution():
    num_packs = 10
    num_cards_per_pack = 20
    uncommon_fraction = 1/4

    # Calculate the total number of cards
    total_cards = num_packs * num_cards_per_pack

    # Calculate the number of uncommon cards
    num_uncommon = total_cards * uncommon_fraction
    result = num_uncommon
    return result

print(solution())