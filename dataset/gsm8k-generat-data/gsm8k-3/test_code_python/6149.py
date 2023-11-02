def solution():
    """A bag of chips weighs 20 ounces, and a tin of cookies weighs 9 ounces. If Jasmine buys 6 bags of chips and 4 times as many tins of cookies, how many pounds does she have to carry?"""
    # Define the weight of a bag of chips and a tin of cookies in pounds
    CHIPS_WEIGHT = 20/16
    COOKIES_WEIGHT = 9/16

    # Define the number of bags of chips and tins of cookies purchased
    bags_of_chips = 6
    tins_of_cookies = 4 * bags_of_chips

    # Calculate the total weight
    total_weight = (bags_of_chips * CHIPS_WEIGHT) + (tins_of_cookies * COOKIES_WEIGHT)

    # Display the total weight
    result = total_weight
    return result

print(solution())