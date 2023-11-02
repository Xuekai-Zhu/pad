def solution():
    
    jimmy_cards = 18
    bob_cards = 3
    mary_cards = 2*bob_cards
    jimmy_cards -= bob_cards + mary_cards
    result = jimmy_cards
    return result

print(solution())