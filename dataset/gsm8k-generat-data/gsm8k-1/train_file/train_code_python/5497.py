def solution():
    """Sasha added 48 cards into a box. Her sister, Karen, then took out 1/6 of the cards Sasha added. If there are now 83 cards in the box, how many cards were originally in the box?"""
    cards_added = 48
    cards_remaining = 83
    fraction_removed = 1/6
    
    cards_before_removal = cards_remaining / (1 - fraction_removed)
    total_cards = cards_before_removal - cards_added
    
    result = total_cards
    return result

print(solution())