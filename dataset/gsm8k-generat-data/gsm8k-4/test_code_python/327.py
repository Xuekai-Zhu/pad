def solution():
    """It takes 15 mink skins to make a coat. Andy buys 30 minks and each mink has 6 babies, but half the total minks are set free by activists. How many coats can he make?"""
    # Define the number of minks purchased by Andy and the number of babies each mink has
    minks_purchased = 30
    mink_babies = 6

    # Calculate the total number of minks after the babies are born
    total_minks = minks_purchased + (minks_purchased * mink_babies)

    # Calculate the number of minks set free by activists
    free_minks = total_minks / 2

    # Calculate the number of minks remaining
    remaining_minks = total_minks - free_minks

    # Calculate the number of coats that can be made
    coats = remaining_minks // 15

    # return the result
    result = coats
    return result

print(solution())