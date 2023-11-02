def solution():
    toothpicks_per_card = 75
    deck_size = 52
    cards_used = deck_size - 16
    num_toothpicks = toothpicks_per_card * cards_used
    toothpick_box_size = 450

    # Calculate the number of boxes of toothpicks used
    num_boxes = num_toothpicks // toothpick_box_size + 1

    result = num_boxes
    return result

print(solution())