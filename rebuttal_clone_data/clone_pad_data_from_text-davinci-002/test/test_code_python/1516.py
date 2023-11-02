def solution():
    blue_pens = 2
    black_pens = 2 * blue_pens
    red_pens = 2 * black_pens - 2
    total_pens = blue_pens + black_pens + red_pens
    result = total_pens
    return result

print(solution())