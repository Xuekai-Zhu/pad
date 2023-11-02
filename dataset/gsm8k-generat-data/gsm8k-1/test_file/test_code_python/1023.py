def solution():
    """A store offers sandwiches in 3 different package sizes: the first package with 2 sandwiches for $3, the second with 4 sandwiches for $6, and a third with 8 sandwiches, but the price is not indicated.
    Knowing that the prices are proportional, how much will the package with 8 sandwiches cost?"""

    # calculate the unit price for each sandwich package
    price_1 = 3 / 2
    price_2 = 6 / 4

    # calculate the unit price for the third package
    # using the ratio of the first two packages
    ratio = price_2 / price_1
    unit_price_3 = price_1 * ratio

    # calculate the total price for the third package
    num_sandwiches_3 = 8
    total_price_3 = num_sandwiches_3 * unit_price_3
    result = total_price_3

    return result

print(solution())