def solution():
    num_cards_per_box = 10
    num_cards_not_in_box = 5
    num_given_away = 2
    num_boxes_left = 5

    # Calculate the total number of cards that were put in boxes
    total_cards_in_boxes = (num_given_away + num_boxes_left) * num_cards_per_box

    # Calculate the total number of cards Robie had in the beginning
    total_cards = total_cards_in_boxes + num_cards_not_in_box
    result = total_cards
    return result

print(solution())