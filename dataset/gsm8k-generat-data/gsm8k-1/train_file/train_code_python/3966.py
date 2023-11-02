def solution():
    """Jordan gave Danielle two dozen roses and a box of chocolates as a birthday day gift. Later that day, after Jordan left, Danielle traded the box of chocolates for another dozen roses. Overnight, half of the roses wilted, and Danielle decided to throw the wilted flowers away. On the second day, another half of the remaining flowers wilted, and she threw the wilted ones away. How many unwilted flowers remained?"""
    initial_roses = 2 * 12 + 1 * 12  # two dozen roses and another dozen traded for box of chocolates
    wilted_roses_day1 = initial_roses // 2
    remaining_roses_day1 = initial_roses - wilted_roses_day1
    wilted_roses_day2 = remaining_roses_day1 // 2
    remaining_roses_day2 = remaining_roses_day1 - wilted_roses_day2
    unwilted_roses = remaining_roses_day2
    result = unwilted_roses
    
    return result

print(solution())