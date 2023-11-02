def solution():
    num_full_decks = 3
    num_half_decks = 3
    num_cards_thrown_away = 34
    cards_per_full_deck = 52
    cards_per_half_deck = cards_per_full_deck / 2
    total_cards = (num_full_decks * cards_per_full_deck) + (num_half_decks * cards_per_half_deck) - num_cards_thrown_away
    result = total_cards
    return result

print(solution())