def solution():
    
    cards_per_box = 10
    cards_not_in_box = 5
    initial_boxes = (2 + 5)
    initial_cards = (initial_boxes * cards_per_box) + cards_not_in_box
    result = initial_cards
    return result

print(solution())