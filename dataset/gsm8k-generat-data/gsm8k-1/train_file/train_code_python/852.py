def solution():
    """Eugene built a model house out of toothpicks and a deck of playing cards. For every card, he used 75 toothpicks. The deck of playing cards had 52 cards, and Eugene used all but 16 of the cards to build his house. If a box of toothpicks contains 450 toothpicks, how many boxes of toothpicks did Eugene use to create his model house?"""
    cards_used = 52 - 16
    toothpicks_per_card = 75
    total_toothpicks = cards_used * toothpicks_per_card
    toothpicks_per_box = 450
    boxes_used = total_toothpicks / toothpicks_per_box
    result = boxes_used
    return result

print(solution())