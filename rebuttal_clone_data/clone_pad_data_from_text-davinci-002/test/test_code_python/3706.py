def solution():
    num_blue_pens = 9
    num_black_pens = 21
    num_red_pens = 6
    pens_removed = 4 + 7
    total_pens = num_blue_pens + num_black_pens + num_red_pens
    pens_left = total_pens - pens_removed
    result = pens_left
    return result

print(solution())