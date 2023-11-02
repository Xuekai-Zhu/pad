def solution():
    """Jimmy has 18 cards. Jimmy gives three cards to Bob. If Jimmy gives Mary twice as many cards as he gave to Bob, how many cards does Jimmy have left?"""
    # Define the initial number of cards Jimmy has
    jimmy_cards = 18

    # Define the number of cards Jimmy gives to Bob
    bob_cards = 3

    # Calculate the number of cards Jimmy gives to Mary
    mary_cards = bob_cards * 2

    # Subtract the total number of cards given away from Jimmy's initial number of cards
    jimmy_cards_left = jimmy_cards - bob_cards - mary_cards

    result = jimmy_cards_left
    return result

print(solution())