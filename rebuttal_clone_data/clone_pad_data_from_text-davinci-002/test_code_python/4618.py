def solution():
    boxes_of_cards = 9
    cards_per_box = 15
    total_cards = boxes_of_cards * cards_per_box
    boxes_of_fc = total_cards / 20
    total_cards = boxes_of_cards + boxes_of_fc
    result = total_cards
    return result

print(solution())