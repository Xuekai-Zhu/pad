def solution():
    chips_weight = 20  # in ounces
    cookies_weight = 9  # in ounces
    num_bags_chips = 6
    num_tins_cookies = 4 * num_bags_chips

    # Calculate the total weight of chips and cookies in ounces
    total_weight = (num_bags_chips * chips_weight) + (num_tins_cookies * cookies_weight)

    # Convert the total weight to pounds
    total_weight_pounds = total_weight / 16.0
    result = total_weight_pounds
    return result

print(solution())