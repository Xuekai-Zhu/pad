def solution():
    num_decks = 16  # Lloyd owns 16 decks of cards
    num_cards_per_deck = 52  # Each deck has 52 cards
    total_cards = num_decks * num_cards_per_deck  # Total number of cards Lloyd has
    num_layers = 32  # Lloyd wants his house to be 32 layers tall

    # Calculate the number of cards per layer that Lloyd needs
    cards_per_layer = total_cards // num_layers
    result = cards_per_layer
    return result

print(solution())