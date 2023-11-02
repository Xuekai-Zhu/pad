def solution():
    """Sasha added 48 cards into a box. Her sister, Karen, then took out 1/6 of the cards Sasha added. If there are now 83 cards in the box, how many cards were originally in the box?"""
    cards_added = 48
    cards_taken_out = cards_added / 6
    remaining_cards = 83
    original_cards = remaining_cards + cards_taken_out
    result = original_cards
    return result

print(solution())