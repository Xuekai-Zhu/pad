def solution():
    """Paul needed to buy some new clothes for work. He had a 10% off coupon that he could use on his entire purchase after any other discounts. Paul bought 4 dress shirts at $15.00 apiece, 2 pairs of pants that each cost $40.00. He found a suit for $150.00 and 2 sweaters for $30.00 each. When he got to the register, the clerk told him that the store was offering 20% off of everything in the store. After the discounts and the coupon, how much did Paul spend on his new clothes?"""

    dress_shirt_price = 15
    num_dress_shirts = 4
    pants_price = 40
    num_pants = 2
    suit_price = 150
    sweater_price = 30
    num_sweaters = 2

    pre_discount_total = dress_shirt_price * num_dress_shirts \
                        + pants_price * num_pants \
                        + suit_price \
                        + sweater_price * num_sweaters

    percent_discount = 20
    discount_amount = pre_discount_total * (percent_discount / 100)
    discounted_total = pre_discount_total - discount_amount

    coupon_percent = 10
    coupon_discount_amount = discounted_total * (coupon_percent / 100)
    final_total = discounted_total - coupon_discount_amount

    result = final_total
    return result

print(solution())