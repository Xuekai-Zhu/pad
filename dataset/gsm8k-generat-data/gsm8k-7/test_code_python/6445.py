def solution():
    num_pink_pens = 12
    num_green_pens = num_pink_pens - 9
    num_blue_pens = num_green_pens + 3

    # Calculate the total number of pens that Tina has
    total_pens = num_pink_pens + num_green_pens + num_blue_pens
    result = total_pens
    return result

print(solution())