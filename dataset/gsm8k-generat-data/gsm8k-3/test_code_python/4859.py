def solution():
    """Lloyd is building a house of cards. He owns 16 decks of cards that have 52 cards each. If each layer of his house of cards has the same exact number of cards, how many cards are there per layer if his house is 32 layers tall?"""
    # Determine the total number of cards available
    num_decks = 16
    cards_per_deck = 52
    total_cards = num_decks * cards_per_deck

    # Determine the number of cards per layer
    num_layers = 32
    cards_per_layer = total_cards // num_layers

    # Display the number of cards per layer
    result = cards_per_layer
    return result

print(solution())