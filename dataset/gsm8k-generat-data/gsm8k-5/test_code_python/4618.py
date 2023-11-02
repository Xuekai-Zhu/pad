def solution():
    basketball_boxes = 9  # Dexter filled 9 plastic boxes with basketball cards
    football_boxes = basketball_boxes - 3  # He filled 3 fewer boxes with football cards than basketball cards

    basketball_cards_per_box = 15  # Each box of basketball cards has 15 cards
    football_cards_per_box = 20  # Each box of football cards has 20 cards

    # Calculate the total number of cards in the basketball boxes
    total_basketball_cards = basketball_boxes * basketball_cards_per_box

    # Calculate the total number of cards in the football boxes
    total_football_cards = football_boxes * football_cards_per_box

    # Add up the total number of cards
    total_cards = total_basketball_cards + total_football_cards
    result = total_cards
    return result

print(solution())