def solution():
    """Roy has 2 blue pens. He has twice as many black and 2 less than twice as many red than black pens. How many pens does Roy have in all?"""
    blue_pens = 2
    black_pens = 2 * blue_pens
    red_pens = 2 * black_pens - 2
    total_pens = blue_pens + black_pens + red_pens
    result = total_pens
    return result

print(solution())