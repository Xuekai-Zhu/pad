def solution():
    """A woman needs to buy 16 oz of butter for a dessert recipe. She can either buy a single 16 oz package of the store-brand butter for $7, or she can buy an 8oz package of store butter for $4 and use a coupon to get an additional two 4 oz packages that normally sell for $2.0 each at a 50% discount (which is applied to each 4oz package separately). What is the lowest price she can pay for the 16 oz of butter she needs?"""
    package_16oz_price = 7
    package_8oz_price = 4
    package_4oz_price = 2
    discount_percent = 50
    discount_amount = package_4oz_price * (discount_percent / 100)
    discounted_price = package_4oz_price - discount_amount
    total_discount_price = (discounted_price * 2) + package_8oz_price
    if total_discount_price < package_16oz_price:
        result = total_discount_price
    else:
        result = package_16oz_price
    return result

print(solution())