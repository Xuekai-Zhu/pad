def solution():
    starting_cards = 20  # Jed starts with 20 cards
    cards_per_week = 6  # Jed gets 6 cards every week
    cards_given_away_every_two_weeks = 2  # Jed gives away 2 cards every two weeks
    target_cards = 40  # Jed wants to have 40 cards

    current_cards = starting_cards
    weeks = 0

    while current_cards < target_cards:
        weeks += 1
        current_cards += cards_per_week
        if weeks % 2 == 0:
            current_cards -= cards_given_away_every_two_weeks

    result = weeks
    return result

print(solution())