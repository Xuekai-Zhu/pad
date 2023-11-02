def solution():
    # Calculate the price of buying a single 16 oz package
    single_price = 7

    # Calculate the price of buying an 8 oz package and two 4 oz packages with a coupon
    package_price = 4 + (2 * 2 * 0.5)

    # Calculate the price per ounce for each option
    single_price_per_oz = single_price / 16
    package_price_per_oz = package_price / 16

    # Determine which option is cheaper and return the lowest price
    if single_price_per_oz < package_price_per_oz:
        result = single_price
    else:
        result = package_price
    return result

print(solution())