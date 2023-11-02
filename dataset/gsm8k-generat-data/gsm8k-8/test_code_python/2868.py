def solution():
    # Define the number of red pens
    red_pens = 8

    # Calculate the number of black and blue pens
    black_pens = red_pens + 10
    blue_pens = red_pens + 7

    # Calculate the total number of pens
    total_pens = red_pens + black_pens + blue_pens
    result = total_pens
    return result

print(solution())