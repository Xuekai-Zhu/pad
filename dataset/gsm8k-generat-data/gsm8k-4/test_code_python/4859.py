def solution():
    """Lloyd is building a house of cards. He owns 16 decks of cards that have 52 cards each. If each layer of his house of cards has the same exact number of cards, how many cards are there per layer if his house is 32 layers tall?"""
    # Define the number of decks and cards per deck
    DECKS = 16
    CARDS_PER_DECK = 52

    # Calculate the total number of cards
    total_cards = DECKS * CARDS_PER_DECK

    # Calculate the number of cards per layer
    cards_per_layer = total_cards / 32

    # round the cards_per_layer and convert it to an integer
    result = int(round(cards_per_layer))
    return result

print(solution())