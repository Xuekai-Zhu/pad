def solution():
    """Aubrey has a deck of cards with 52 cards in it. She then adds two additional cards to the deck. If she splits the deck evenly among herself and two other players, how many cards does each player have?"""
    # Define the number of cards in the deck
    original_deck = 52

    # Define the number of additional cards added
    additional_cards = 2

    # Calculate the total number of cards
    total_cards = original_deck + additional_cards

    # Divide the cards evenly among three players
    cards_per_player = total_cards // 3

    # Display the number of cards each player has
    result = cards_per_player
    return result

print(solution())