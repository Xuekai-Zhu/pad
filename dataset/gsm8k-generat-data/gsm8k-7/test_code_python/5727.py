def solution():
    num_white_daisies = 6

    # Calculate the number of pink daisies
    num_pink_daisies = num_white_daisies * 9

    # Calculate the number of red daisies
    num_red_daisies = (4 * num_pink_daisies) - 3

    # Calculate the total number of daisies
    total_daisies = num_white_daisies + num_pink_daisies + num_red_daisies
    result = total_daisies
    return result

print(solution())