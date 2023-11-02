def solution():
    # Calculate the number of toothpicks used in the model house
    num_cards_used = 52 - 16  # Eugene used all but 16 cards to build his house
    num_toothpicks_used = num_cards_used * 75  # for every card, Eugene used 75 toothpicks
    num_boxes_used = num_toothpicks_used // 450  # a box of toothpicks contains 450 toothpicks
    result = num_boxes_used
    return result

print(solution())