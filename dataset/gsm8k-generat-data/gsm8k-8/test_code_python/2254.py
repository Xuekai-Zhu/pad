def solution():
    # Add two cards to the deck
    total_cards = 52 + 2

    # Split the deck evenly among three players
    cards_per_player = total_cards // 3

    result = cards_per_player
    return result

print(solution())