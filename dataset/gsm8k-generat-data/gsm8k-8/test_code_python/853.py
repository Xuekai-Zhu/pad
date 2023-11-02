def solution():
    # Calculate the number of cards used
    cards_used = 52 - 16

    # Calculate the total number of toothpicks used
    toothpicks_used = cards_used * 75

    # Calculate the number of boxes of toothpicks used
    boxes_used = toothpicks_used / 450

    result = boxes_used
    return result

print(solution())