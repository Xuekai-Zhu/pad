def solution():
    
    decks_of_cards = 16
    cards_per_deck = 52
    total_cards = decks_of_cards * cards_per_deck
    layers = 32
    cards_per_layer = total_cards / layers
    result = cards_per_layer
    return result

print(solution())