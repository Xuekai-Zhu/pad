def solution():
    """A bag of chips weighs 20 ounces, and a tin of cookies weighs 9 ounces. If Jasmine buys 6 bags of chips and 4 times as many tins of cookies, how many pounds does she have to carry?"""
    # Define the weight of a bag of chips and a tin of cookies in ounces
    CHIP_WEIGHT_OZ = 20
    COOKIE_WEIGHT_OZ = 9

    # Define the number of bags of chips and tins of cookies Jasmine buys
    bags_of_chips = 6
    tins_of_cookies = 4 * bags_of_chips

    # Calculate the total weight in ounces
    total_weight_oz = (bags_of_chips * CHIP_WEIGHT_OZ) + (tins_of_cookies * COOKIE_WEIGHT_OZ)

    # Convert the weight from ounces to pounds
    total_weight_lbs = total_weight_oz / 16

    # Return the result
    result = total_weight_lbs
    return result

print(solution())