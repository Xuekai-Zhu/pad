def solution():
    """A woman needs to buy 16 oz of butter for a dessert recipe. She can either buy a single 16 oz package of the store-brand butter for $7, or she can buy an 8oz package of store butter for $4 and use a coupon to get an additional two 4 oz packages that normally sell for $2.0 each at a 50% discount (which is applied to each 4oz package separately).  What is the lowest price she can pay for the 16 oz of butter she needs?"""
    # Define the prices of different butter packages
    package_16oz_price = 7
    package_8oz_price = 4
    package_4oz_price = 2

    # Calculate the price of buying two 4 oz packages with a 50% discount
    package_4oz_discounted_price = package_4oz_price * 0.5

    # Calculate the total price of buying one 8 oz package and two 4 oz packages with discount
    total_price_with_coupon = package_8oz_price + (2 * package_4oz_discounted_price)

    # Compare the prices and choose the lower one
    if total_price_with_coupon < package_16oz_price:
        lowest_price = total_price_with_coupon
    else:
        lowest_price = package_16oz_price

    result = lowest_price
    return result

print(solution())