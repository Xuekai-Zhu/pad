def solution():
    """Dexter filled 3 fewer plastic boxes with football cards than basketball cards. He filled 9 boxes with basketball cards and each box has 15 cards. For the boxes with football cards, he filled each box with 20 cards. How many cards does Dexter have in total?"""
    # Define the number of boxes of basketball cards
    bball_boxes = 9

    # Calculate the number of boxes of football cards
    fb_boxes = bball_boxes - 3

    # Calculate the total number of basketball cards
    bball_cards = bball_boxes * 15

    # Calculate the total number of football cards
    fb_cards = fb_boxes * 20

    # Calculate the total number of cards
    total_cards = bball_cards + fb_cards

    # Display the total number of cards
    result = total_cards
    return result

print(solution())