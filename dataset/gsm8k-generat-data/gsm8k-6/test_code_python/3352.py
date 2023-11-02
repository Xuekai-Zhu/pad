def solution():
    # Find the number of blue pens in Sam's collection
    blue_pens = 2 * 8  # twice as many blue pens as pencils
    # Find the number of black pens in Sam's collection
    black_pens = blue_pens + 10  # ten more black pens than blue pens
    # Find the number of red pens in Sam's collection
    red_pens = 8 - 2  # two fewer red pens than pencils
    # Calculate the total number of pens in Sam's collection
    total_pens = blue_pens + black_pens + red_pens
    result = total_pens
    return result

print(solution())