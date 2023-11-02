def solution():
    original_price = 125  # Todd paid $125 for the jeans at full price
    sale_price = original_price * 0.8  # The jeans were on sale for 20% off
    coupon_price = sale_price - 10  # Todd applied a $10 coupon to the sale price
    card_price = coupon_price * 0.9  # Todd paid with a store credit card that gave him another 10% off

    # Calculate how much Todd saved on the original price of the jeans
    saved_amount = original_price - card_price
    result = saved_amount
    return result

print(solution())