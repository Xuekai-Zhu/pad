def solution():
    jimmy_cards = 18  # Jimmy has 18 cards
    bob_cards = 3  # Jimmy gives 3 cards to Bob
    mary_cards = 2 * bob_cards  # Mary gets twice as many cards as Bob

    # Calculate the total number of cards given away
    total_given_away = bob_cards + mary_cards

    # Calculate the number of cards Jimmy has left
    cards_left = jimmy_cards - total_given_away
    result = cards_left
    return result

print(solution())