def solution():
    """Sasha added 48 cards into a box. Her sister, Karen, then took out 1/6 of the cards Sasha added. If there are now 83 cards in the box, how many cards were originally in the box?"""
    # Define the number of cards Sasha added
    added_cards = 48

    # Calculate the number of cards Karen took out
    removed_cards = added_cards / 6

    # Calculate the number of cards in the box originally
    original_cards = 83 + removed_cards

    # Display the original number of cards
    result = original_cards
    return result

print(solution())