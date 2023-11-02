def solution():
    """Dexter filled 3 fewer plastic boxes with football cards than basketball cards. He filled 9 boxes with basketball cards and each box has 15 cards. For the boxes with football cards, he filled each box with 20 cards. How many cards does Dexter have in total?"""
    # Calculate the number of boxes filled with football cards
    football_boxes = 9 - 3

    # Calculate the total number of basketball cards
    basketball_cards = 9 * 15

    # Calculate the total number of football cards
    football_cards = football_boxes * 20

    # Calculate the total number of cards
    total_cards = basketball_cards + football_cards

    # return the result
    result = total_cards
    return result

print(solution())