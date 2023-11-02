def solution():
    """There are 48 passengers on the bus. Two-thirds of the passengers are women and the rest are men.  If one-eighth of the men are standing, how many men are seated?"""
    # Calculate the number of women on the bus
    women = 48 * (2/3)

    # Calculate the number of men on the bus
    men = 48 - women

    # Calculate the number of men standing
    men_standing = men / 8

    # Calculate the number of men seated
    men_seated = men - men_standing

    # Display the number of men seated
    result = men_seated
    return result

print(solution())