def solution():
    # Define the number of cards Jame can tear in a week
    cards_per_week = 30 * 3

    # Calculate the total number of cards in 18 decks
    total_cards = 55 * 18

    # Calculate the number of weeks Jame can tear cards
    weeks_can_go = total_cards // cards_per_week
    result = weeks_can_go
    return result

print(solution())