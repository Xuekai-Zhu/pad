def solution():
    weight_chips = 20  # A bag of chips weighs 20 ounces
    weight_cookies = 9  # A tin of cookies weighs 9 ounces
    bags_of_chips = 6  # Jasmine buys 6 bags of chips
    tins_of_cookies = 4 * bags_of_chips  # Jasmine buys 4 times as many tins of cookies

    # Calculate the total weight in ounces
    total_weight = (weight_chips * bags_of_chips) + (weight_cookies * tins_of_cookies)

    # Convert the total weight to pounds
    total_weight_pounds = total_weight / 16
    result = total_weight_pounds
    return result

print(solution())