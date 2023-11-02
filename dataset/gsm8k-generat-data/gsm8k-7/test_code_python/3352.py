def solution():
    blue_pens = 0
    black_pens = 0
    red_pens = 0
    pencils = 8

    # Calculate the number of blue pens
    blue_pens = 2 * pencils

    # Calculate the number of black pens
    black_pens = blue_pens + 10

    # Calculate the number of red pens
    red_pens = pencils - 2

    # Calculate the total number of pens
    total_pens = blue_pens + black_pens + red_pens
    result = total_pens
    return result

print(solution())