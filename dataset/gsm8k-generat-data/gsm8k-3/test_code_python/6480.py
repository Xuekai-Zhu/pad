def solution():
    """Hannah collects mugs. She already has 40 different mugs in 4 different colors. She has three times more blue mugs than red mugs and 12 yellow mugs. Considering that she has only half as many red mugs as yellow mugs, how many mugs of another color than mentioned does she have?"""
    # Define the number of different colored mugs Hannah has
    DIFF_COLOR_MUGS = 4

    # Define the number of different colored mugs Hannah has, excluding the ones mentioned
    OTHER_COLOR_MUGS = DIFF_COLOR_MUGS - 3

    # Define the number of red mugs Hannah has
    red_mugs = 0.5 * 12

    # Define the number of blue mugs Hannah has in terms of red mugs
    blue_mugs = 3 * red_mugs

    # Calculate the total number of mugs Hannah has
    total_mugs = 40 + red_mugs + blue_mugs + 12

    # Calculate the number of mugs of another color than mentioned
    other_color_mugs = total_mugs - (red_mugs + blue_mugs + 12)

    # Display the number of mugs of another color than mentioned
    result = other_color_mugs
    return result

print(solution())