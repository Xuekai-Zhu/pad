def solution():
    """Eugene built a model house out of toothpicks and a deck of playing cards. For every card, he used 75 toothpicks. The deck of playing cards had 52 cards, and Eugene used all but 16 of the cards to build his house. If a box of toothpicks contains 450 toothpicks, how many boxes of toothpicks did Eugene use to create his model house?"""
    # Define the number of cards used in the model house
    cards_used = 52 - 16

    # Calculate the total number of toothpicks used
    toothpicks_used = cards_used * 75

    # Calculate the number of toothpick boxes used
    boxes_used = toothpicks_used / 450

    # Round up to the nearest whole number of boxes
    boxes_used = math.ceil(boxes_used)

    # return the result
    result = boxes_used
    return result

print(solution())