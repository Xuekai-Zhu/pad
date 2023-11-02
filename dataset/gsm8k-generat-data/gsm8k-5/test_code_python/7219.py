def solution():
    shirt_price = 15.00  # Price of one dress shirt
    pants_price = 40.00  # Price of one pair of pants
    suit_price = 150.00  # Price of the suit
    sweater_price = 30.00  # Price of one sweater
    num_shirts = 4  # Paul bought 4 dress shirts
    num_pants = 2  # Paul bought 2 pairs of pants
    num_sweaters = 2  # Paul bought 2 sweaters

    # Calculate the total cost without any discounts or coupons
    total_cost = (shirt_price * num_shirts) + (pants_price * num_pants) + suit_price + (sweater_price * num_sweaters)

    # Calculate the discount from the 20% off offer
    discount = total_cost * 0.2

    # Calculate the discounted price
    discounted_price = total_cost - discount

    # Calculate the discount from the coupon
    coupon_discount = discounted_price * 0.1

    # Calculate the final price after all discounts and coupons
    final_price = discounted_price - coupon_discount
    result = final_price
    return result

print(solution())