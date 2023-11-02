def solution():
    # Define the initial number of pens
    blue_pens = 9
    black_pens = 21
    red_pens = 6

    # Remove 4 blue pens and 7 black pens
    blue_pens -= 4
    black_pens -= 7

    # Calculate the total number of remaining pens
    total_pens = blue_pens + black_pens + red_pens
    result = total_pens
    return result

print(solution())