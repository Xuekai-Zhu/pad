def solution():
    # Calculate the cost of the shirts
    shirts_cost = 4 * 15.00

    # Calculate the cost of the pants
    pants_cost = 2 * 40.00

    # Calculate the cost of the suit
    suit_cost = 150.00

    # Calculate the cost of the sweaters
    sweaters_cost = 2 * 30.00

    # Calculate the total cost before any discounts
    total_cost = shirts_cost + pants_cost + suit_cost + sweaters_cost

    # Calculate the discount from the store's offer
    store_discount = 0.20 * total_cost

    # Calculate the total cost after the store discount
    total_cost_after_discount = total_cost - store_discount

    # Calculate the discount from the coupon
    coupon_discount = 0.10 * total_cost_after_discount

    # Calculate the total cost after all discounts
    total_cost_after_all_discounts = total_cost_after_discount - coupon_discount

    result = total_cost_after_all_discounts
    return result

print(solution())