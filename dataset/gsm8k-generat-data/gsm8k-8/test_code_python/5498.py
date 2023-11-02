def solution():
    # Define the number of cards Sasha added
    sasha_added = 48

    # Calculate the number of cards Karen took out
    karen_removed = sasha_added / 6

    # Calculate the remaining number of cards after Karen's removal
    remaining_cards = 83

    # Calculate the original number of cards in the box
    original_cards = remaining_cards + karen_removed
    result = original_cards
    return result

print(solution())