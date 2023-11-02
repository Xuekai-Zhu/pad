def solution():
    cards_in_deck = 52
    additional_cards = 2
    total_cards = cards_in_deck + additional_cards
    cards_per_player = total_cards / 3
    result = cards_per_player
    return result

print(solution())