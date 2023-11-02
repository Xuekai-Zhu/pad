def solution():
    """Lloyd is building a house of cards. He owns 16 decks of cards that have 52 cards each. If each layer of his house of cards has the same exact number of cards, how many cards are there per layer if his house is 32 layers tall?"""
    decks_of_cards = 16
    cards_per_deck = 52
    total_cards = decks_of_cards * cards_per_deck
    layers = 32
    cards_per_layer = total_cards / layers
    result = cards_per_layer
    return result

print(solution())