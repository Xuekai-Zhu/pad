def solution():
    """Of 96 oranges, half were ripe. If 1/4 of the ripe oranges were eaten and 1/8 of the unripe oranges were eaten, how many were left uneaten in total?"""
    total_oranges = 96
    ripe_oranges = total_oranges / 2
    unripe_oranges = total_oranges - ripe_oranges
    eaten_ripe = ripe_oranges / 4
    eaten_unripe = unripe_oranges / 8
    uneaten_oranges = total_oranges - (eaten_ripe + eaten_unripe)
    result = uneaten_oranges
    return result

print(solution())