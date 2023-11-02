def solution():
    """Marla is mixing a particular shade of lilac that's 70% blue paint, 20% red paint, and the rest white paint. If she adds 140 ounces of blue paint, how many ounces of white paint does she add?"""
    blue_percent = 70
    red_percent = 20
    white_percent = 100 - blue_percent - red_percent
    blue_amount = 140
    white_amount = (blue_amount / blue_percent) * white_percent
    result = white_amount
    return result

print(solution())