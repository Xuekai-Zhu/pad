def solution():
    # Calculate the total weight of the chips and cookies in ounces
    chips_weight = 20 * 6  # Jasmine buys 6 bags of chips
    cookies_weight = 9 * 4 * 6  # Jasmine buys 4 times as many tins of cookies
    total_weight = chips_weight + cookies_weight

    # Convert the total weight from ounces to pounds
    weight_in_pounds = total_weight / 16  # There are 16 ounces in a pound
    result = weight_in_pounds
    return result

print(solution())