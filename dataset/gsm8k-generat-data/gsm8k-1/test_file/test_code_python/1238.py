def solution():
    """Skyler has 100 hats on his hand with the colors red, blue, and white. Half of the hats are red, 3/5 of the remaining hats are blue, and the rest are white. How many white hats does Skyler have?"""
    total_hats = 100
    red_hats = total_hats / 2
    remaining_hats = total_hats - red_hats
    blue_hats = remaining_hats * (3/5)
    white_hats = total_hats - red_hats - blue_hats
    result = white_hats
    return result

print(solution())