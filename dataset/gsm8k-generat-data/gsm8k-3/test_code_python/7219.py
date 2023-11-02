def solution():
    """Paul needed to buy some new clothes for work.  He had a 10% off coupon that he could use on his entire purchase after any other discounts.  Paul bought 4 dress shirts at $15.00 apiece, 2 pairs of pants that each cost $40.00.  He found a suit for $150.00 and 2 sweaters for $30.00 each.  When he got to the register, the clerk told him that the store was offering 20% off of everything in the store.  After the discounts and the coupon, how much did Paul spend on his new clothes?"""
    # Define the prices of the items Paul bought
    SHIRT_PRICE = 15
    PANTS_PRICE = 40
    SUIT_PRICE = 150
    SWEATER_PRICE = 30

    # Define the number of each item Paul bought
    num_shirts = 4
    num_pants = 2
    num_suits = 1
    num_sweaters = 2

    # Calculate the total cost before any discounts
    total_cost = num_shirts * SHIRT_PRICE + num_pants * PANTS_PRICE + num_suits * SUIT_PRICE + num_sweaters * SWEATER_PRICE

    # Calculate the discount from the store's sale
    sale_discount = 0.2 * total_cost

    # Subtract the sale discount from the total cost
    total_cost -= sale_discount

    # Calculate the discount from Paul's coupon
    coupon_discount = 0.1 * total_cost

    # Subtract the coupon discount from the total cost
    total_cost -= coupon_discount

    # Display the final cost
    result = total_cost
    return result

print(solution())