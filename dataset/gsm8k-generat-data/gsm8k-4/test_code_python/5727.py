def solution():
    """ Jack is making flower crowns out of red, pink and white daisies. There are nine times as many pink daisies as white daisies and three less than four times as many red daisies as pink daisies. If there are 6 white daisies, how many daisies are there total?"""
    # Define the number of white daisies
    white_daisies = 6

    # Calculate the number of pink daisies
    pink_daisies = white_daisies * 9

    # Calculate the number of red daisies
    red_daisies = 4 * pink_daisies - 3

    # Calculate the total number of daisies
    total_daisies = white_daisies + pink_daisies + red_daisies

    # return the result
    result = total_daisies
    return result

print(solution())