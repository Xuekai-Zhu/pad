def solution():
    """Sasha added 48 cards into a box. Her sister, Karen, then took out 1/6 of the cards Sasha added. If there are now 83 cards in the box, how many cards were originally in the box?"""
    # Define the number of cards Sasha initially added to the box
    original_cards = None

    # Calculate the number of cards Karen took out
    cards_removed = 1/6 * 48

    # Calculate the current number of cards in the box
    current_cards = 83

    # Calculate the original number of cards in the box
    original_cards = current_cards - cards_removed - 48

    result = original_cards
    return result

print(solution())