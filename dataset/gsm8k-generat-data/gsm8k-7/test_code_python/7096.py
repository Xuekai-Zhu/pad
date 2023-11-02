def solution():
    regular_price = 15.00
    discount = 0.20     # 20% discount
    num_bottles = 3
    coupon_value = 2.00

    # Calculate the price of one bottle after discount
    discounted_price = regular_price * (1 - discount)

    # Calculate the total cost for three bottles before coupons
    total_cost_before_coupons = num_bottles * discounted_price

    # Calculate the total discount from the coupons
    total_coupon_discount = num_bottles * coupon_value

    # Calculate the final cost for three bottles after the coupons are applied
    final_cost = total_cost_before_coupons - total_coupon_discount
    result = final_cost
    return result

print(solution())