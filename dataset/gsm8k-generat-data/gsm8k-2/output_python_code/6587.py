def solution():
    """A jar contains 9 blue pens, 21 black pens, and 6 red pens. Four blue pens are removed and then seven black pens are removed. How many pens are left in the jar?"""
    blue_pens = 9
    black_pens = 21
    red_pens = 6
    blue_pens -= 4
    black_pens -= 7
    total_pens_left = blue_pens + black_pens + red_pens
    result = total_pens_left
    return result

print(solution())