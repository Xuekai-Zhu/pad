def solution():
    num_cards = 52 + 2  # 52 cards in the original deck, plus 2 additional cards
    num_players = 3

    # Calculate the number of cards each player gets if the deck is split evenly
    cards_per_player = num_cards / num_players
    result = cards_per_player
    return result

print(solution())