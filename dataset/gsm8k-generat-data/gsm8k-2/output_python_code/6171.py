def solution():
    """Jimmy has 18 cards. Jimmy gives three cards to Bob. If Jimmy gives Mary twice as many cards as he gave to Bob, how many cards does Jimmy have left?"""
    jimmy_cards = 18
    bob_cards = 3
    mary_cards = 2*bob_cards
    jimmy_cards -= bob_cards + mary_cards
    result = jimmy_cards
    return result

print(solution())