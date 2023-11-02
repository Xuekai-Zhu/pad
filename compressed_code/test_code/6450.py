def solution():
    
    cards_used = 52 - 16
    toothpicks_per_card = 75
    total_toothpicks = cards_used * toothpicks_per_card
    toothpicks_per_box = 450
    boxes_used = total_toothpicks / toothpicks_per_box
    result = boxes_used
    return result

print(solution())