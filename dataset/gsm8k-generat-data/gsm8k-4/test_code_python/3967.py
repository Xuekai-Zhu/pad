def solution():
    """Jordan gave Danielle two dozen roses and a box of chocolates as a birthday day gift. Later that day, after Jordan left, Danielle traded the box of chocolates for another dozen roses. Overnight, half of the roses wilted, and Danielle decided to throw the wilted flowers away. On the second day, another half of the remaining flowers wilted, and she threw the wilted ones away. How many unwilted flowers remained?"""
    # Define the initial number of roses
    initial_roses = 2 * 12 + 1 * 12

    # Calculate the number of roses remaining after the first night
    first_night_roses = initial_roses / 2

    # Calculate the number of roses remaining after the second night
    second_night_roses = first_night_roses / 2

    # Calculate the number of unwilted roses remaining
    unwilted_roses = second_night_roses

    # return the result
    result = unwilted_roses
    return result

print(solution())