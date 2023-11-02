def solution():
    # Calculate the number of plastic boxes filled with football cards
    football_boxes = 9 - 3  # Dexter filled 3 fewer plastic boxes with football cards than basketball cards

    # Calculate the number of cards in the basketball boxes
    basketball_cards = 9 * 15  # he filled 9 boxes with basketball cards and each box has 15 cards

    # Calculate the number of cards in the football boxes
    football_cards = football_boxes * 20  # he filled each football box with 20 cards

    # Calculate the total number of cards
    total_cards = basketball_cards + football_cards

    result = total_cards
    return result

print(solution())