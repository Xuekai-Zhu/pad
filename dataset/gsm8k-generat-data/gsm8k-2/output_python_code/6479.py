def solution():
    """Hannah collects mugs. She already has 40 different mugs in 4 different colors. She has three times more blue mugs than red mugs and 12 yellow mugs. Considering that she has only half as many red mugs as yellow mugs, how many mugs of another color than mentioned does she have?"""
    total_mugs = 40
    total_colors = 4
    yellow_mugs = 12
    red_mugs = yellow_mugs / 2
    blue_mugs = 3 * red_mugs
    total_colored_mugs = yellow_mugs + red_mugs + blue_mugs
    other_mugs = total_mugs - total_colored_mugs
    result = other_mugs
    return result

print(solution())