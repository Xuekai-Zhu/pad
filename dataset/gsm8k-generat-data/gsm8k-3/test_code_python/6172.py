def solution():
    """Jimmy has 18 cards. Jimmy gives three cards to Bob. If Jimmy gives Mary twice as many cards as he gave to Bob, how many cards does Jimmy have left?"""
    # Jimmy starts with 18 cards
    jimmy_cards = 18

    # Jimmy gives 3 cards to Bob
    bob_cards = 3
    jimmy_cards -= bob_cards

    # Jimmy gives twice as many cards to Mary as he gave to Bob
    mary_cards = 2 * bob_cards
    jimmy_cards -= mary_cards

    # Jimmy has some cards left
    result = jimmy_cards
    return result

print(solution())