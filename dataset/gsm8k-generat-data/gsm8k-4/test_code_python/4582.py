def solution():
    """Robie filled some plastic boxes with hockey cards. There were 10 cards in each box but 5 cards were not placed in a box. He gave away 2 boxes to his friends and he has 5 boxes with him. How many cards did Robie have in the beginning?"""
    # Define the number of cards in each box and the number of boxes
    cards_per_box = 10
    boxes_given_away = 2
    boxes_remaining = 5

    # Calculate the total number of boxes
    total_boxes = boxes_given_away + boxes_remaining

    # Calculate the total number of cards in the boxes
    total_cards_in_boxes = (total_boxes * cards_per_box) - 5

    # Calculate the total number of cards that Robie had in the beginning
    total_cards = total_cards_in_boxes + 5

    result = total_cards
    return result

print(solution())