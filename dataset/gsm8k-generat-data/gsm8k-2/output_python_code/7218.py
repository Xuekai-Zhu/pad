def solution():
    """
    Paul needed to buy some new clothes for work. He had a 10% off coupon that he could use on his entire purchase after any other discounts.
    Paul bought 4 dress shirts at $15.00 apiece, 2 pairs of pants that each cost $40.00.
    He found a suit for $150.00 and 2 sweaters for $30.00 each.
    When he got to the register, the clerk told him that the store was offering 20% off of everything in the store.
    After the discounts and the coupon, how much did Paul spend on his new clothes?
    """
    dress_shirt_cost = 15
    pants_cost = 40
    suit_cost = 150
    sweater_cost = 30
    num_dress_shirts = 4
    num_pants = 2
    num_sweaters = 2
    total_cost = (
        num_dress_shirts * dress_shirt_cost
        + num_pants * pants_cost
        + suit_cost
        + num_sweaters * sweater_cost
    )
    discount = 0.2
    discounted_cost = total_cost - (total_cost * discount)
    coupon_discount = 0.1
    final_cost = discounted_cost - (discounted_cost * coupon_discount)
    result = final_cost
    return result

print(solution())