def solution():
    
    # Define the number of small coupons and the cost per small coupon
    small_coupons = 700
    small_coupon_cost = 0.05

    # Define the number of big coupons and the cost per big coupon
    big_coupons = 2 * small_coupons
    big_coupon_cost = 0.15

    # Calculate the total cost of the coupons
    total_cost = (small_coupons * small_coupon_cost) + (big_coupons * big_coupon_cost)

    # return the result
    result = total_cost
    return result

print(solution())