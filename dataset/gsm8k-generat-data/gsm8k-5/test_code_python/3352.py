def solution():
    blue_pens = 2 * 8  # Twice as many blue pens as pencils, where there are 8 pencils
    black_pens = blue_pens + 10  # Ten more black pens than blue pens
    red_pens = 8 - 2  # Two fewer red pens than pencils, where there are 8 pencils
    total_pens = blue_pens + black_pens + red_pens  # Total number of pens in Sam's collection

    result = total_pens
    return result

print(solution())