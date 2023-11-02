def solution():
    """Jordan gave Danielle two dozen roses and a box of chocolates as a birthday day gift.  Later that day, after Jordan left, Danielle traded the box of chocolates for another dozen roses.  Overnight, half of the roses wilted, and  Danielle decided to throw the wilted flowers away.  On the second day, another half of the remaining flowers wilted, and she threw the wilted ones away.  How many unwilted flowers remained?"""
    # Define the initial number of roses
    initial_roses = 2 * 12 + 1 * 12

    # Calculate the number of roses remaining after the first night
    remaining_roses_1 = initial_roses // 2

    # Calculate the number of roses remaining after the second night
    remaining_roses_2 = remaining_roses_1 // 2

    # Calculate the number of unwilted roses remaining
    unwilted_roses = remaining_roses_2

    # Display the number of unwilted roses remaining
    result = unwilted_roses
    return result

print(solution())