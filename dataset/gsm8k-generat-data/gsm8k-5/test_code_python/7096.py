def solution():
    regular_price = 15.0  # price of one bottle of vitamins before discount and coupons
    discount_percentage = 0.2  # 20% discount
    discounted_price = regular_price * (1 - discount_percentage)  # price of one bottle after discount
    num_bottles = 3  # number of bottles Ken wants to buy
    coupon_value = 2.0  # value of one coupon

    # Calculate the total cost of the bottles after discount and coupons
    total_cost = (discounted_price * num_bottles) - (coupon_value * 3)

    result = total_cost
    return result

print(solution())