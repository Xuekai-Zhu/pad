def solution():
    minks = 30 + (30*6)  # Andy buys 30 minks and each mink has 6 babies
    minks_set_free = minks / 2  # Half of the minks are set free by activists
    minks_to_use = minks - minks_set_free  # The number of minks to use in making coats

    # Calculate the number of coats that can be made
    coats = minks_to_use // 15  # It takes 15 mink skins to make one coat
    result = coats
    return result

print(solution())