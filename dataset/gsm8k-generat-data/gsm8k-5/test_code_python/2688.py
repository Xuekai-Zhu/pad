def solution():
    blue_pens = 2  # Roy has 2 blue pens

    # Roy has twice as many black pens as blue pens
    black_pens = 2 * blue_pens

    # Roy has 2 less than twice as many red pens as black pens
    red_pens = 2 * black_pens - 2

    # Calculate the total number of pens Roy has
    total_pens = blue_pens + black_pens + red_pens
    result = total_pens
    return result

print(solution())