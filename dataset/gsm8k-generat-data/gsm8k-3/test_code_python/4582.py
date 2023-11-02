def solution():
    """Robie filled some plastic boxes with hockey cards. There were 10 cards in each box but 5 cards were not placed in a box. He gave away 2 boxes to his friends and he has 5 boxes with him. How many cards did Robie have in the beginning?"""
    # Define the number of boxes filled with cards and the number of cards per box
    total_boxes = 7
    cards_per_box = 10

    # Calculate the total number of cards placed in boxes
    cards_in_boxes = (total_boxes - 2) * cards_per_box

    # Calculate the total number of cards without boxes
    cards_without_boxes = 5

    # Calculate the total number of cards Robie had in the beginning
    total_cards = cards_in_boxes + cards_without_boxes

    # Display the total number of cards
    result = total_cards
    return result

print(solution())