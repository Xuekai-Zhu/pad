def solution():
    """A man is purchasing a pair of sneakers at a club store where he receives a membership discount of 10% off any purchase. In addition to the membership discount, the man also has a coupon for $10 off any pair of sneakers. If the man wants to purchase a $120 pair of sneakers and the membership discount must be applied after the coupon, how much will he pay for the sneakers after using both the coupon and membership discount?"""
    # Define the original price of the sneakers
    original_price = 120

    # Apply the coupon discount
    coupon_discounted_price = original_price - 10

    # Apply the membership discount
    final_price = coupon_discounted_price * 0.9

    result = final_price
    return result

print(solution())