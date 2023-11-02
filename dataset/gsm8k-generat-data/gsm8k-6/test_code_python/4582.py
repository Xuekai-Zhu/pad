def solution():
    # Calculate the total number of hockey cards Robie had in the beginning
    total_boxes = 2 + 5  # Robie gave away 2 boxes and has 5 boxes with him
    total_cards = (total_boxes * 10) + 5  # there were 10 cards in each box and 5 cards were not placed in a box
    result = total_cards
    return result

print(solution())