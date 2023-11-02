def solution():
    cards_given_to_bob = 3
    cards_given_to_mary = cards_given_to_bob * 2
    total_cards_given_away = cards_given_to_bob + cards_given_to_mary
    initial_card_count = 18
    cards_left = initial_card_count - total_cards_given_away
    result = cards_left
    return result

print(solution())