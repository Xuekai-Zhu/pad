def solution():
    # Calculate the number of blue pens
    pencils = 8
    blue_pens = 2 * pencils
    black_pens = blue_pens + 10

    # Calculate the number of red pens
    red_pens = pencils - 2

    # Calculate the total number of pens
    total_pens = blue_pens + black_pens + red_pens
    result = total_pens
    return result

print(solution())