def solution():
    num_half_full_decks = 3
    num_full_decks = 3
    cards_per_deck = 52
    cards_lost = 34

    # Calculate the total number of cards John had before throwing any away
    total_cards = (num_half_full_decks * cards_per_deck // 2) + (num_full_decks * cards_per_deck)

    # Calculate the total number of cards John has after throwing some away
    total_cards_after_trash = total_cards - cards_lost
    result = total_cards_after_trash
    return result

print(solution())