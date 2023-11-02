def solution():
    # Add the two additional cards to the deck
    total_cards = 52 + 2

    # Divide the deck evenly among 3 players
    cards_per_player = total_cards // 3

    result = cards_per_player
    return result

print(solution())