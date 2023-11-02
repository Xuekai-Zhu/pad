def solution():
    # Calculate the original cost of Paul's purchase before any discounts
    original_cost = (4 * 15) + (2 * 40) + 150 + (2 * 30)  # cost of 4 dress shirts, 2 pants, 1 suit, and 2 sweaters
    # Calculate the amount saved with the 20% discount
    discount = 0.2 * original_cost
    # Calculate the new cost after the 20% discount
    new_cost = original_cost - discount
    # Calculate the amount saved with the 10% coupon
    coupon_discount = 0.1 * new_cost
    # Calculate the final cost after the coupon discount
    final_cost = new_cost - coupon_discount
    result = final_cost
    return result

print(solution())