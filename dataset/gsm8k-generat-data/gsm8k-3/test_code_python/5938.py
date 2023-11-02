def solution():
    """A man is purchasing a pair of sneakers at a club store where he receives a membership discount of 10% off any purchase.  In addition to the membership discount, the man also has a coupon for $10 off any pair of sneakers.  If the man wants to purchase a $120 pair of sneakers and the membership discount must be applied after the coupon, how much will he pay for the sneakers after using both the coupon and membership discount?"""
    # Define the original cost of the sneakers
    ORIGINAL_COST = 120

    # Apply the coupon to get the discounted cost
    discounted_cost = ORIGINAL_COST - 10

    # Apply the membership discount to get the final cost
    final_cost = discounted_cost * 0.9

    # Display the final cost
    result = final_cost
    return result

print(solution())