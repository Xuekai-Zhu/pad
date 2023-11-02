def solution():
    # Calculate the total number of pens Roy has
    black_pens = 2 * 2  # Roy has twice as many black pens as blue pens
    red_pens = 2 * black_pens - 2  # Roy has 2 less than twice as many red pens than black pens
    total_pens = 2 + black_pens + red_pens  # Roy has 2 blue pens, black pens, and red pens
    result = total_pens
    return result

print(solution())