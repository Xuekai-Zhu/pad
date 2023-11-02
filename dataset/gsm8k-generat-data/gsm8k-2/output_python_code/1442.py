def solution():
    """Todd bought a pair of jeans that cost $125 at full price. The jeans were on sale for 20% off. He then applied a coupon that took off $10. He paid with a store credit card that gave him another 10% off the remaining amount. How many dollars did he save on the original price of the jeans?"""
    original_price = 125
    sale_price = original_price * 0.8
    coupon_price = sale_price - 10
    remaining_price = coupon_price * 0.9
    saved_price = original_price - remaining_price
    result = saved_price
    return result

print(solution())