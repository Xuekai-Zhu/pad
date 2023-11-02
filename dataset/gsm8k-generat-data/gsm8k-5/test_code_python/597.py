def solution():
    full_decks = 3  # John has 3 full decks of cards
    cards_per_deck = 52  # Each deck of cards should have 52 cards
    half_full_decks = 3  # John has 3 half-full decks of cards
    cards_removed = 34  # John threw 34 cards in the trash

    # Calculate the total number of cards John has before throwing some away
    total_cards_before = full_decks * cards_per_deck + (half_full_decks * cards_per_deck) / 2

    # Calculate the total number of cards John has after throwing some away
    total_cards_after = total_cards_before - cards_removed

    result = total_cards_after
    return result

print(solution())