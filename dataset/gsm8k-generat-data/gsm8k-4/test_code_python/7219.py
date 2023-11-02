def solution():
    """Paul needed to buy some new clothes for work.  He had a 10% off coupon that he could use on his entire purchase after any other discounts.  Paul bought 4 dress shirts at $15.00 apiece, 2 pairs of pants that each cost $40.00.  He found a suit for $150.00 and 2 sweaters for $30.00 each.  When he got to the register, the clerk told him that the store was offering 20% off of everything in the store.  After the discounts and the coupon, how much did Paul spend on his new clothes?"""
    # Define the prices of the clothes
    shirt_price = 15
    pant_price = 40
    suit_price = 150
    sweater_price = 30

    # Calculate the total cost of the clothes before any discounts
    total_cost = (4 * shirt_price) + (2 * pant_price) + suit_price + (2 * sweater_price)

    # Calculate the discount from the store's 20% off sale
    store_discount = total_cost * 0.2

    # Calculate the discounted cost of the clothes after the store's discount
    discounted_cost = total_cost - store_discount

    # Calculate the discount from Paul's 10% off coupon
    coupon_discount = discounted_cost * 0.1

    # Calculate the final cost of the clothes after all discounts
    final_cost = discounted_cost - coupon_discount

    # return the result
    result = final_cost
    return result

print(solution())