def solution():
    total_cost = 54.0
    discount_percentage = 0.2  # 20% discount
    item_discounted_price = 20.0 * (1 - discount_percentage)
    coupon_percentage = 0.1  # 10% coupon

    # Calculate the total cost with the discounted item
    total_cost = total_cost - 20.0 + item_discounted_price

    # Calculate the total cost with the coupon
    total_cost = total_cost * (1 - coupon_percentage)
    result = total_cost
    return result

print(solution())