def solution():
    # Define the number of white daisies
    white_daisies = 6

    # Calculate the number of pink daisies
    pink_daisies = 9 * white_daisies

    # Calculate the number of red daisies
    red_daisies = 4 * pink_daisies - 3

    # Calculate the total number of daisies
    total_daisies = white_daisies + pink_daisies + red_daisies
    result = total_daisies
    return result

print(solution())