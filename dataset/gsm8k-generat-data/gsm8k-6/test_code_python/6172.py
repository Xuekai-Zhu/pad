def solution():
    # Jimmy gives Bob 3 cards
    bob_cards = 3
    # Jimmy gives Mary twice as many cards as he gave Bob
    mary_cards = 2*bob_cards
    # Total cards given away
    total_given = bob_cards + mary_cards
    # Subtract total given cards from Jimmy's original cards
    cards_left = 18 - total_given
    result = cards_left
    return result

print(solution())