def solution():
    """Eugene built a model house out of toothpicks and a deck of playing cards.  For every card, he used 75 toothpicks.  The deck of playing cards had 52 cards, and Eugene used all but 16 of the cards to build his house.  If a box of toothpicks contains 450 toothpicks, how many boxes of toothpicks did Eugene use to create his model house?"""
    # Define the number of toothpicks used per card
    TOOTHPICKS_PER_CARD = 75

    # Define the number of cards used
    cards_used = 52 - 16

    # Calculate the total number of toothpicks used
    total_toothpicks = cards_used * TOOTHPICKS_PER_CARD

    # Calculate the number of boxes of toothpicks used
    boxes_used = total_toothpicks / 450

    # Round up to the nearest whole number of boxes
    boxes_used = math.ceil(boxes_used)

    # Display the number of boxes of toothpicks used
    result = boxes_used
    return result

print(solution())