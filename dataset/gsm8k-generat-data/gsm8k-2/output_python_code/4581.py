def solution():
    """Robie filled some plastic boxes with hockey cards. There were 10 cards in each box but 5 cards were not placed in a box. He gave away 2 boxes to his friends and he has 5 boxes with him. How many cards did Robie have in the beginning?"""
    cards_per_box = 10
    unused_cards = 5
    given_away_boxes = 2
    remaining_boxes = 5
    total_cards = (given_away_boxes + remaining_boxes) * cards_per_box - unused_cards
    result = total_cards
    return result

print(solution())