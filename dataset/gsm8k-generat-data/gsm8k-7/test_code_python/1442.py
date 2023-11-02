def solution():
    # Define the given values
    cards_per_tear = 30
    cards_in_deck = 55
    tears_per_week = 3
    num_decks = 18

    # Calculate the total number of tears per week
    total_tears_per_week = tears_per_week * cards_per_tear

    # Calculate the total number of cards in all the decks
    total_cards = num_decks * cards_in_deck

    # Calculate the total number of weeks Jame can go
    total_weeks = total_cards // total_tears_per_week
    result = total_weeks
    return result

print(solution())