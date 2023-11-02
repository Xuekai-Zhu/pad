def solution():
    num_cans = 9
    discount_per_coupon = 0.25
    num_coupons = 5
    total_paid = 20
    change_received = 5.5

    # Calculate the total discount from using the coupons
    total_discount = discount_per_coupon * num_coupons

    # Calculate the total cost of all cans of tuna before discounts or change
    total_cost = total_paid - change_received + total_discount

    # Calculate the cost of a single can of tuna in cents
    price_per_can = total_cost / num_cans * 100
    result = price_per_can
    return result

print(solution())