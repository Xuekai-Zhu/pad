def solution():
    # Calculate the total number of cards and the number of uncommon cards in a pack
    cards_per_pack = 20
    uncommon_per_pack = cards_per_pack * (1/4)

    # Calculate the total number of uncommon cards John got
    total_uncommon_cards = 10 * uncommon_per_pack

    result = total_uncommon_cards
    return result

print(solution())