def solution():
    """Hannah collects mugs. She already has 40 different mugs in 4 different colors. She has three times more blue mugs than red mugs and 12 yellow mugs. Considering that she has only half as many red mugs as yellow mugs, how many mugs of another color than mentioned does she have?"""
    total_mugs = 40
    total_colors = 4
    red_mugs = total_mugs // total_colors
    yellow_mugs = 12
    blue_mugs = 3 * red_mugs
    other_mugs = total_mugs - (red_mugs + yellow_mugs + blue_mugs)
    result = other_mugs
    return result

print(solution())