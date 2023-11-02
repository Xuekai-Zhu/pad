def solution():
    """Sam is stocking up on canned tuna. He got 9 cans at the supermarket, and had 5 coupons for 25 cents off a single can per coupon. He paid $20 and got $5.50 in change. How many cents does a can of tuna cost?"""
    # Define the number of cans and the coupon discount
    NUM_CANS = 9
    COUPON_DISCOUNT = 0.25

    # Define the total cost and the change received
    total_cost = 2000
    change_received = 550

    # Calculate the total discount from the coupons
    coupon_discount_total = 5 * COUPON_DISCOUNT

    # Calculate the cost of the cans before the discount
    cans_cost_before_discount = total_cost - change_received + coupon_discount_total

    # Calculate the cost per can after the discount
    can_cost = cans_cost_before_discount / NUM_CANS

    # Convert the cost to cents
    cents_per_can = can_cost * 100

    # Display the cost per can in cents
    result = cents_per_can
    return result

print(solution())