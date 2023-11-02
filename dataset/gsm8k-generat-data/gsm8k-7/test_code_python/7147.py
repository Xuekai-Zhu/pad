def solution():
    cards_per_week = 6
    give_away_interval = 2
    cards_given_away = 2
    starting_cards = 20
    target_cards = 40

    # Calculate how many weeks it takes to accumulate the target number of cards
    weeks = 0
    cards = starting_cards
    while cards < target_cards:
        weeks += 1
        cards += cards_per_week
        if weeks % give_away_interval == 0:
            cards -= cards_given_away

    result = weeks
    return result

print(solution())