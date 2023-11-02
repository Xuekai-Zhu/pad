def solution():
    cards_per_deck = 55  # Each deck has 55 cards
    cards_per_tear = 30  # Jame can tear 30 cards at a time
    tears_per_week = 3  # Jame tears cards 3 times a week
    decks = 18  # Jame buys 18 decks of cards

    # Calculate the total number of tears Jame can make with 18 decks
    total_tears = decks * cards_per_deck / cards_per_tear

    # Calculate the number of weeks Jame can go tearing cards
    weeks = total_tears / tears_per_week
    result = weeks
    return result

print(solution())