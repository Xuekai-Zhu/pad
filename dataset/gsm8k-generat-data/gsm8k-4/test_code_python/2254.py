def solution():
    """Aubrey has a deck of cards with 52 cards in it. She then adds two additional cards to the deck. If she splits the deck evenly among herself and two other players, how many cards does each player have?"""
    # Define the total number of cards in the deck
    total_cards = 52 + 2

    # Calculate the number of cards each player will have
    cards_per_player = total_cards // 3

    result = cards_per_player
    return result

print(solution())