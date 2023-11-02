def solution():
    b_boxes = 9
    b_cards_per_box = 15

    f_boxes = b_boxes - 3
    f_cards_per_box = 20

    # Calculate the total number of basketball cards
    total_b_cards = b_boxes * b_cards_per_box

    # Calculate the total number of football cards
    total_f_cards = f_boxes * f_cards_per_box

    # Calculate the total number of cards
    total_cards = total_b_cards + total_f_cards
    result = total_cards
    return result

print(solution())