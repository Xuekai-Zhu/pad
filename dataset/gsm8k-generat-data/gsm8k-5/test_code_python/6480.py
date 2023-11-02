def solution():
    # Calculate the number of red mugs
    red_mugs = 12 / 2  # Hannah has only half as many red mugs as yellow mugs

    # Calculate the number of blue mugs
    blue_mugs = 3 * red_mugs  # Hannah has three times more blue mugs than red mugs

    # Calculate the total number of mugs Hannah has
    total_mugs = 40 + red_mugs + blue_mugs + 12  # Hannah has 40 different mugs in 4 different colors, 12 yellow mugs, and some red and blue mugs

    # Calculate the number of mugs of another color than mentioned
    other_mugs = total_mugs - 40 - red_mugs - blue_mugs - 12
    result = other_mugs
    return result

print(solution())