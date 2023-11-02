def solution():
    """Marla is mixing a particular shade of lilac that's 70% blue paint, 20% red paint, and the rest white paint. If she adds 140 ounces of blue paint, how many ounces of white paint does she add?"""
    blue_percentage = 0.7
    red_percentage = 0.2
    white_percentage = 1 - blue_percentage - red_percentage
    blue_added = 140
    white_added = (blue_added / blue_percentage) * white_percentage
    result = white_added
    return result

print(solution())