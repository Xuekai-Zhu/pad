def solution():
    """Hannah collects mugs. She already has 40 different mugs in 4 different colors. She has three times more blue mugs than red mugs and 12 yellow mugs. Considering that she has only half as many red mugs as yellow mugs, how many mugs of another color than mentioned does she have?"""
    # Define the number of different colors of mugs Hannah already has
    colors = 4

    # Define the number of mugs Hannah already has
    total_mugs = 40

    # Define the number of yellow mugs Hannah has
    yellow_mugs = 12

    # Calculate the number of red mugs Hannah has
    red_mugs = yellow_mugs // 2

    # Calculate the number of blue mugs Hannah has
    blue_mugs = 3 * red_mugs

    # Calculate the total number of mugs Hannah has of the mentioned colors
    mentioned_mugs = yellow_mugs + red_mugs + blue_mugs

    # Calculate the number of mugs of another color than mentioned
    other_mugs = total_mugs - mentioned_mugs

    result = other_mugs
    return result

print(solution())