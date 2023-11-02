def solution():
    """It takes 15 mink skins to make a coat. Andy buys 30 minks and each mink has 6 babies, but half the total minks are set free by activists. How many coats can he make?"""
    # Define the number of mink skins needed to make a coat and the number of minks Andy buys
    SKINS_PER_COAT = 15
    minks_bought = 30

    # Calculate the number of minks after they have babies
    minks_with_babies = minks_bought * 6

    # Calculate the total number of minks
    total_minks = minks_bought + minks_with_babies

    # Calculate the number of minks that are set free by activists
    minks_set_free = total_minks / 2

    # Calculate the number of mink skins Andy has left after the activists set some free
    skins_left = (total_minks - minks_set_free) * 2

    # Calculate the number of coats Andy can make with the remaining skins
    coats = skins_left // SKINS_PER_COAT

    # Display the number of coats Andy can make
    result = coats
    return result

print(solution())