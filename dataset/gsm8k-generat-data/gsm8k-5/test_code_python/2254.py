def solution():
    total_cards = 52 + 2  # Aubrey has 52 cards in her deck, plus 2 additional cards
    num_players = 3  # Aubrey wants to split the deck evenly among herself and two other players

    # Calculate the number of cards each player receives
    cards_per_player = total_cards // num_players

    result = cards_per_player
    return result

print(solution())