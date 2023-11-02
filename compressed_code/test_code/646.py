def solution():
    
    cards_used = 52 - 16
    toothpicks_per_card = 75
    total_toothpicks = cards_used * toothpicks_per_card
    toothpicks_per_box = 450
    num_boxes = total_toothpicks / toothpicks_per_box
    result = num_boxes
    return result

print(solution())