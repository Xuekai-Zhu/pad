def solution():
    num_blue_pens = 9
    num_black_pens = 21
    num_red_pens = 6

    # Remove 4 blue pens
    num_blue_pens -= 4

    # Remove 7 black pens
    num_black_pens -= 7

    # Calculate the total number of pens left in the jar
    total_pens = num_blue_pens + num_black_pens + num_red_pens
    result = total_pens
    return result

print(solution())