def solution():
    """Erica made 20 Valentine's cards to pass out. Her dad brought her 2 boxes of pre-made Valentine's cards that had 15 cards each. She passed out 24 to her classmates, 5 to her family and received 17 from family and friends. How many Valentine's Day cards does Erica now have?"""
    erica_cards = 20
    pre_made_cards = 2 * 15
    classmate_cards = 24
    family_cards_given = 5
    cards_received = 17
    total_cards = erica_cards + pre_made_cards + cards_received - classmate_cards - family_cards_given
    result = total_cards
    return result

print(solution())