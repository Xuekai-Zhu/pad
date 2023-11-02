def solution():
    """Aubrey has a deck of cards with 52 cards in it. She then adds two additional cards to the deck. If she splits the deck evenly 
    among herself and two other players, how many cards does each player have?"""
    initial_cards = 52
    extra_cards = 2
    total_cards = initial_cards + extra_cards
    players = 3
    cards_per_player = total_cards // players
    result = cards_per_player
    return result

print(solution())