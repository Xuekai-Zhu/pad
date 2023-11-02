def solution():
    """Jordan gave Danielle two dozen roses and a box of chocolates as a birthday day gift. Later that day, after Jordan left, Danielle traded the box of chocolates for another dozen roses. Overnight, half of the roses wilted, and Danielle decided to throw the wilted flowers away. On the second day, another half of the remaining flowers wilted, and she threw the wilted ones away. How many unwilted flowers remained?"""
    initial_roses = 2 * 12 + 1 * 12  # 24+12=36
    first_day_roses = initial_roses / 2  # 36/2=18
    second_day_roses = first_day_roses / 2  # 18/2=9
    unwilted_roses = second_day_roses
    result = unwilted_roses
    return result

print(solution())