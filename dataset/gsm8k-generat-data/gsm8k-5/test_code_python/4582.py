def solution():
    cards_per_box = 10  # There are 10 cards in each box
    cards_not_in_box = 5  # There are 5 cards that were not placed in a box
    initial_total_boxes = len(cards_not_in_box) + 2 + 5  # Robie gave away 2 boxes and kept 5 boxes

    # Calculate the initial number of cards Robie had
    initial_total_cards = (initial_total_boxes - 2) * cards_per_box + cards_not_in_box
    result = initial_total_cards
    return result

print(solution())