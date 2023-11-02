def solution():
    # Calculate the total number of cards Jame can tear
    total_cards = 30 * 3  # Jame tears 30 cards at a time, 3 times a week

    # Calculate the total number of cards in 18 decks
    total_decks = 18
    cards_per_deck = 55
    total_cards_in_decks = total_decks * cards_per_deck

    # Calculate the number of weeks Jame can go
    weeks = total_cards_in_decks // total_cards
    result = weeks
    return result

print(solution())