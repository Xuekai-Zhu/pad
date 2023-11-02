def solution():
    toothpicks_per_card = 75  # Eugene used 75 toothpicks for every playing card
    total_cards = 52  # There are 52 playing cards in a deck
    cards_used = total_cards - 16  # Eugene used all but 16 cards to build his house
    total_toothpicks = toothpicks_per_card * cards_used  # Calculate the total number of toothpicks used

    # Calculate the number of boxes of toothpicks used
    boxes_of_toothpicks = total_toothpicks / 450

    result = boxes_of_toothpicks
    return result

print(solution())