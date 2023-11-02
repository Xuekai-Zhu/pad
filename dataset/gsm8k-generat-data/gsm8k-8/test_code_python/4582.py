def solution():
    # Calculate the total number of cards in the boxes Robie gave away
    cards_given_away = 2 * 10

    # Calculate the total number of cards in the boxes Robie has left
    cards_left = 5 * 10 + 5

    # Calculate the total number of cards Robie had in the beginning
    total_cards = cards_given_away + cards_left
    result = total_cards
    return result

print(solution())