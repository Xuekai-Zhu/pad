def solution():
    """Ken buys gummy vitamins. They are usually $15.00 per bottle at his grocery store, but they are currently 20% off. On top of that, he has 3 $2.00 coupons. How much will 3 bottles cost?"""
    bottle_price = 15.0
    discount_percent = 20
    discount_amount = bottle_price * discount_percent / 100
    discounted_price = bottle_price - discount_amount
    coupon_amount = 2.0
    num_bottles = 3
    total_price = num_bottles * discounted_price - (3 * coupon_amount)
    result = total_price
    return result

print(solution())