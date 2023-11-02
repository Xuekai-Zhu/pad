def solution():
    """It takes 15 mink skins to make a coat. Andy buys 30 minks and each mink has 6 babies, but half the total minks are set free by activists. How many coats can he make?"""
    minks_bought = 30
    baby_minks = minks_bought * 6
    total_minks = minks_bought + baby_minks
    minks_set_free = total_minks / 2
    minks_for_coats = total_minks - minks_set_free
    coats = minks_for_coats // 15
    result = coats
    return result

print(solution())