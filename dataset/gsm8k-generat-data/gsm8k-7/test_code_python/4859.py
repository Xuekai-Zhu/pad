def solution():
    num_decks = 16
    num_cards_per_deck = 52
    num_layers = 32

    # Calculate the total number of cards that Lloyd has
    total_cards = num_decks * num_cards_per_deck

    # Calculate the number of cards per layer
    cards_per_layer = total_cards / num_layers
    result = cards_per_layer
    return result

print(solution())